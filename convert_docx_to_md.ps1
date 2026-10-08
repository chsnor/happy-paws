Add-Type -AssemblyName System.IO.Compression.FileSystem

function Convert-DocxToMarkdown {
    param (
        [string]$DocxPath,
        [string]$MdPath
    )

    if (-not (Test-Path $DocxPath)) {
        Write-Error "File not found: $DocxPath"
        return
    }

    $zip = [System.IO.Compression.ZipFile]::OpenRead($DocxPath)
    $entry = $zip.GetEntry('word/document.xml')
    if (-not $entry) {
        $zip.Dispose()
        Write-Error "word/document.xml not found in $DocxPath"
        return
    }

    $stream = $entry.Open()
    $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::UTF8)
    $xmlContent = $reader.ReadToEnd()
    $reader.Dispose()
    $stream.Dispose()
    $zip.Dispose()

    [xml]$doc = $xmlContent
    $ns = New-Object System.Xml.XmlNamespaceManager($doc.NameTable)
    $ns.AddNamespace("w", "http://schemas.openxmlformats.org/wordprocessingml/2006/main")

    $output = [System.Collections.Generic.List[string]]::new()

    $bodyNodes = $doc.SelectNodes("/w:document/w:body/*", $ns)

    foreach ($node in $bodyNodes) {
        if ($node.LocalName -eq "p") {
            # Check paragraph style / heading
            $pStyle = $node.SelectSingleNode("w:pPr/w:pStyle/@w:val", $ns)
            $styleVal = if ($pStyle) { $pStyle.Value } else { "" }
            
            $numPr = $node.SelectSingleNode("w:pPr/w:numPr", $ns)

            # Get text fragments
            $pText = ""
            $textRuns = $node.SelectNodes(".//w:r", $ns)
            foreach ($r in $textRuns) {
                $bold = $r.SelectSingleNode("w:rPr/w:b", $ns) -ne $null
                $italic = $r.SelectSingleNode("w:rPr/w:i", $ns) -ne $null
                $code = ($r.SelectSingleNode("w:rPr/w:rFonts[@w:ascii='Courier New' or @w:ascii='Consolas']", $ns) -ne $null)

                $runText = ""
                foreach ($child in $r.ChildNodes) {
                    if ($child.LocalName -eq "t") {
                        $runText += $child.InnerText
                    } elseif ($child.LocalName -eq "br") {
                        $runText += "`n"
                    } elseif ($child.LocalName -eq "tab") {
                        $runText += "    "
                    }
                }

                if ($runText.Length -gt 0) {
                    if ($bold -and -not $italic) {
                        $pText += "**" + $runText + "**"
                    } elseif ($italic -and -not $bold) {
                        $pText += "*" + $runText + "*"
                    } elseif ($bold -and $italic) {
                        $pText += "***" + $runText + "***"
                    } else {
                        $pText += $runText
                    }
                }
            }

            if ([string]::IsNullOrWhiteSpace($pText)) {
                $output.Add("")
                continue
            }

            if ($styleVal -match "^Heading(\d+)$" -or $styleVal -match "^heading\s*(\d+)$") {
                $level = [int]$Matches[1]
                $prefix = "#" * $level
                $output.Add("$prefix $pText")
                $output.Add("")
            } elseif ($styleVal -match "^Title$") {
                $output.Add("# $pText")
                $output.Add("")
            } elseif ($styleVal -match "^Subtitle$") {
                $output.Add("## $pText")
                $output.Add("")
            } elseif ($numPr -ne $null) {
                $output.Add("- $pText")
            } else {
                $output.Add($pText)
                $output.Add("")
            }
        } elseif ($node.LocalName -eq "tbl") {
            # Process table
            $rows = $node.SelectNodes("w:tr", $ns)
            $isFirstRow = $true
            foreach ($tr in $rows) {
                $cells = $tr.SelectNodes("w:tc", $ns)
                $cellTexts = @()
                foreach ($tc in $cells) {
                    $paragraphs = $tc.SelectNodes("w:p", $ns)
                    $cellPTexts = @()
                    foreach ($p in $paragraphs) {
                        $tNodes = $p.SelectNodes(".//w:t", $ns)
                        $tStr = ($tNodes | ForEach-Object { $_.InnerText }) -join ""
                        if (-not [string]::IsNullOrWhiteSpace($tStr)) {
                            $cellPTexts += $tStr.Trim()
                        }
                    }
                    $cellVal = ($cellPTexts -join " <br> ").Replace("|", "\|")
                    $cellTexts += $cellVal
                }
                $rowLine = "| " + ($cellTexts -join " | ") + " |"
                $output.Add($rowLine)

                if ($isFirstRow) {
                    $sep = "| " + (($cellTexts | ForEach-Object { "---" }) -join " | ") + " |"
                    $output.Add($sep)
                    $isFirstRow = $false
                }
            }
            $output.Add("")
        }
    }

    [System.IO.File]::WriteAllLines($MdPath, $output, [System.Text.Encoding]::UTF8)
    Write-Output "Converted: $DocxPath -> $MdPath"
}

# Convert both documents
Convert-DocxToMarkdown -DocxPath "D:\fullstack\Claude Code MariaDB 1 unfinished.docx" -MdPath "D:\fullstack\Claude Code MariaDB 1 unfinished.md"
Convert-DocxToMarkdown -DocxPath "D:\fullstack\Full-Stack AI Application Lesson 1-4 students.docx" -MdPath "D:\fullstack\Full-Stack AI Application Lesson 1-4 students.md"

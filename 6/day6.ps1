[Reflection.Assembly]::LoadFile("C:\Users\devfour\Documents\Hackvent.2017\BarcodeLib.BarcodeReader.dll")

$path = "C:\tmp\day6"
$a = @()

$b = new-object BarcodeLib.BarcodeReader.BarcodeReader
for($i=0;$i -lt 1000;$i++)
{
    $png =(new-object System.Net.WebClient).DownloadData("http://challenges.hackvent.hacking-lab.com:4200")
    #$a +=, $png
    [io.file]::WriteAllBytes($path+"\tmp.png", $png)
    [string] $qr = [BarcodeLib.BarcodeReader.BarcodeReader]::read($path+"\tmp.png", [BarcodeLib.BarcodeReader.BarcodeReader]::QRCODE)

    if ($qr.ToLower().Contains("hv17") -or $qr.ToLower().Contains("4v17"))
    {
        Write-Host $qr
        break
    }
}

#$a = $a | Select -Unique

<#for($i=0;$i -lt $a.Count;$i++)
{
    [io.file]::WriteAllBytes($path+"\"+$i+".png", $a[$i])
}

Get-ChildItem -Path $path | Sort-Object -Property Length
#>


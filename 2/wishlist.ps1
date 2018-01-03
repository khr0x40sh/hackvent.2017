Param($wishlist="Wishlist.txt")

$gather=""

function b64decode{
Param($string1)
    $raw=[System.Convert]::FromBase64String($string1)
    $out = [System.Text.Encoding]::ASCII.GetString($raw)
    $out
}

foreach($line in Get-Content $wishlist)
 {
    [string]$x=$line.ToString()
    $gather+=$x
 }

 for ($i=0; $i -lt 32; $i++)
 {
    $x = b64decode $gather
    $gather=$x
 }
 $gather

 <# OR #>

$a = Get-Content "Wishlist.txt"; for($i=0;$i -lt 32;$i++){$b=[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($a));$a=$b;}$a
 
 

 
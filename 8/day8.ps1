$a = Get-content "True.1337"

$b=$a -split "`n"
$top =""
$bottom=""
$bb = $b[0] -split "chr"
$bbb = $b[1] -split "_1337"
foreach ($str in $bb)
{
    $count = ([regex]::Matches($str, "True" )).count
    
    $char = [char]$count
    $top += $char
}

foreach ($str in $bbb)
{
    $check = $str.split("(")[0]
   
    if ($check -eq "__1337"){
            $str -replace "__1337", "exec"
        $bottom += $str
    }
    else
    {
        $intA = $str.split("+")
        $i=0
        foreach ($int in $intA)
        {
            try
            {
                $int = $int.Trim("(")
                $int = $int.Trim(")")
                $i += [System.Int32]::Parse($int)
            }
            catch{ }
        }
        $num =  ($i / 1337)
        $s =''
        if (($num -lt 32) -or ($num -gt 127))
        {
            $s = "\x"+('{0:x2}' -f $num).ToString()
        }
        else
        {
            $s = [char] $num
        }
        $bottom +=$s
    }

}

$top
$bottom


#stage2
$x=@(0x7B, 0x67, 0x05, 0x06, 0x18, 0x4D, 0x5A, 0x07, 0x46, 0x1E, 0x5F, 0x4D, 0x0C, 0x43, 0x14, 0x5F, 0x03, 0x58, 0x0B, 0x19, 0x5C, 0x07, 0x45, 0x52, 0x1E, 0x46, 0x5B, 0x58, 0x13)
$y="31415926535897932384626433832".ToCharArray()
$z = ""
for($i =0; $i -lt $y.Count;$i++)
{
    $z += [char]($x[$i] -bxor [int][char]$y[$i])
} 
$z



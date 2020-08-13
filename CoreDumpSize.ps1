###############################################################################
#
# Script to get size of core dumps in Bytes. This will be used to throw an
# alert every time a new core dump file is created.
#
###############################################################################
# Version: 1.0		28.06.2016 Christoph Vossieg CI/BEE2
#					initial version
# Version: 1.1		15.07.2016 Christoph Vossieg CI/BEE2
#					updated directory
# Version: 1.2		16.08.2016 Christoph Vossieg CI/BEE2
#					added foreach loop to check every installed JTS version
# Version: 1.3      20.10.2017 Sven Koch CI/OSE2
#                   added Test-Path checks to make sure that the checked dirs
#                   exist
# Version: 1.4      23.10.2017 Sven Koch CI/OSE2
#                   added functions and the possibility to monitor Liberty
# Version: 1.5		23.10.2017 Sven Koch CI/OSE2
#                   Fixed Liberty monitoring by selecting the latest
# Version: 1.6      14.05.2018 Christoph Vossieg CI/OSE2
#                   modified directory to use new dumps directory for 6.0.5
###############################################################################


# fixspan: time span to regard changes in the core dump files

$fixspan = New-TimeSpan -Days 0 -hour 0 -minute -2

function checkFile([string]$directory, [string]$fixspan)
{
    if (Test-Path $directory)
    {
        foreach ($file in (dir $directory))
        {
            if ($file -like "*core*")
            {
                $date = Get-Date
                $timespan = $file.LastWriteTime - $date
                if ($timespan -gt $fixspan)
                {
                    $colItems = ($file | Measure-Object -property length -sum)
                    [int] $size = ($colItems.sum / 1024)
                    write-output ("Name: " + $file.Name + " Last Modified: " + $file.LastWriteTime + " Size in KB: " + $size + " Location: " + $directory)
                    Start-Sleep -Milliseconds 1000
                }    
            }
        }
    }
}

# Search in WebSphere, deprecated in 6.0.5
function checkWebSphere()
{
    $dir = "D:\IBM\WebSphere\AppServer\profiles\AppSrv01\"
    # Check in all core dump files if the file was changed during the fixspan and write an output
    checkFile $dir $fixspan
}

# Search in WebSphere Liberty, deprecated in 6.0.5
function checkLiberty()
{
	#Get Latest Liberty / Jazz Folder
    if (Test-Path "D:\IBM\JazzTeamServer-*")
    {
        $dir = Get-ChildItem -Path D:\IBM\ -Name "JazzTeamServer-*" | Sort-Object -Descending | Select-Object -First 1
        $dir= "D:\IBM\$dir\server\liberty\servers\clm\"
        checkFile $dir $fixspan
    }
}

# Search in JTS Folders, deprecated in 6.0.5
function checkJazzFolder()
{
    $dir = "D:\IBM\"
    # Check in all core dump files if the file was changed during the fixspan and write an output
    if (Test-Path $dir)
    {
        foreach ($file in (dir $dir))
        {
            if ($file -match "JazzTeamServer-*")
            {
                $subdir=$dir + $file.Name + "\server"
                if (Test-Path $subdir)
                {
                    foreach ($file in (dir $subdir))
                    {
                        if ($file -like "*core*")
                        {
                            $date = Get-Date
                            $timespan = $file.LastWriteTime - $date
                            if ($timespan -gt $fixspan)
                            {
                                $colItems = ($file | Measure-Object -property length -sum)
                                [int] $size = ($colItems.sum / 1024)
                                write-output ("Name: " + $file.Name + " Last Modified: " + $file.LastWriteTime + " Size in KB: " + $size + " Location: " + $subdir)
                                Start-Sleep -Milliseconds 1000
                            }
                        }
                    }  
                }
                else
                {
                    exit 0
                }
            }
        }
    }
}

#Do stuff..
$dir = "D:\IBM\dumps\"
checkFile $dir $fixspan

# Deprecated in 6.0.5
checkWebSphere
checkLiberty
checkJazzFolder
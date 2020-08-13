$file_data = [xml](Get-Content C:\Users\nte1cob\Desktop\test.xml)
$version=$file_data.installInfo.location.package

foreach ($file in $version)
        {
            if($file.name="IBM WebSphere Application Server"){
                write-output($file)
                }
            
        }


#write-output ("id - "+$version.id)
#Write-Output("Version - "+$version.version)
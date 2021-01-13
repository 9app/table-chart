#$HTML = python.exe .\run.py '.\csv\file' '.\csv\file1' '.\csv\file2'
$HTML = get-content .\temp.html

$outlook = New-Object -ComObject Outlook.Application

$Mail = $outlook.CreateItem(0)
$Mail.Sender = 'kamal242@outlook.com'
$Mail.To = 'kamal242@outlook.com'
$Mail.Subject = 'Test Mail'
$Mail.HTMLBody = "$HTML"

$files = Get-ChildItem W:\Dropbox\PROJECTS\Flask\Outlook-Email3\img

for ($i=0; $i -lt $files.count; $i++) {
    $Mail.Attachments.Add($files[$i].fullName)
}
$Mail.Send()
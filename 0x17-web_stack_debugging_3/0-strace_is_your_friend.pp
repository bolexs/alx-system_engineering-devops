# Fix 500 server error when a GET request is made to the Apache web server

$file_to_edit = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}

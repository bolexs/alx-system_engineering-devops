# Fix 500 server error when a GET request is made to the Apache web server

$file_edited = '/var/www/html/wp-settings.php'

exec {'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_edited}",
  path => ['/bin', '/usr/bin']
}

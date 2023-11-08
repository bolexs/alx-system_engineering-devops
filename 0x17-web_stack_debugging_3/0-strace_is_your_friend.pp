# Fix 500 server error when a GET request is made to the Apache web server

exec {'fix-wp':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path => '/usr/local/bin/:/bin/'
}

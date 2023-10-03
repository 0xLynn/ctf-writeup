# Zerion

> <p>We observed some odd network traffic, and found this file on our web server... can you find the strange domains that our systems are reaching out to?</p>
> <p>NOTE, this challenge is based off of a real malware sample. We have done our best to "defang" the code, but out of abudance of caution it is strongly encouraged you only analyze this inside of a virtual environment separate from any production devices.</p>
> <p><a href="attachments/zerion">zerion</a></p>

## Path to Flag

The PHP Script given was obfuscated, so I used a tool from `https://github.com/simon816/PHPDeobfuscator`

`php index.php -f ./zerion`

<a href="attachments/deobfuscated.txt">Deobfuscated PHP Script</a>

The flag was written in plaintext.

`cat deobfuscated.txt | grep flag`

`flag{af10370d485952897d5183aa09e19883}`
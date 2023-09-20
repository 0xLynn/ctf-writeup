# Absence Makes Hearts Go Yonder

> <p>Sometimes the oldest and simplest tricks can be the most fun. Here's an old stego tactic that requires no special software - just a little knowledge and maybe a keen eye.</p>
> <p><img src="attachments/stego1.gif"></p>

## Path to Flag

I started of with checking the metadata and found nothing, but found something hidden by using `binwalk`

<img src="attachments/binwalk.png">

Extract the hidden file and read the `flag`

<img src="attachments/flag.png">

`poctf{uwsp_h342d_y0u_7h3_f1257_71m3}`
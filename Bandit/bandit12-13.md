# Solution

First, we need to convert the hexdump into something more useful(probably ascii or binary)

To do that:
	`xxd -r data.txt <filename_u_want>`

Now using the **file** command, we can check for various compression techniques. For each technique use the following procedure:

## gzip

1. convert the file_name into file_name.gz
2. decompress using the command: `gzip -d file_name.gz`

## tar

1. convert the file_name into file_name.tar
2. decompress using the command: `tar -xvf file_name.tar`

## bzip2

1. Simply use the command: `bzip2 -d file_name`

password: `5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu`



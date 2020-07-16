# May as well check everything, hmm? Good. :D
# This isn't really it, but you should keep going. There's another node worthy
# of your attention. An encrypted one. Maybe the passphrase you have didn't
# work?
# I got my name from this book, a book in the Hebrew bible. That book has a
#classification. That's the passphrase. All lower case, mind! Old man Qoheleth
# is lazy. :D

.PHONY: all
all: blockintopost qr map nodes upload backup full

.PHONY: blockintopost
blockintopost: aesblock gpgblock
	cd stories && perl -0777 -MFile::Slurp -i.bak -lne '$$aes=read_file("aesblock.asc") and ~s/(BLOCK-----\n).+(-----END)/\1$${aes}\2/sm and print' qoheleth-1.md

.PHONY: aesblock
aesblock:
	aescrypt -e -p kemmer -o stories/aesblock.aes stories/aesblock.txt
	base64 -b 64 -i stories/aesblock.aes -o stories/aesblock.asc

.PHONY: gpgblock
gpgblock:
	gpg -u 0670aab1 -r 0670aab1 -sea --for-your-eyes-only --yes -o stories/qoheleth-5.md.asc stories/qoheleth-5.md

.PHONY: qr
qr: checkpayloads
	cat payloads/payload-1.yaml | qrencode -s 20 -m 2 -o qr/qr-1.png
	cat payloads/payload-2.yaml | qrencode -s 20 -m 2 -o qr/qr-2.png
	cat payloads/payload-3.yaml | qrencode -s 20 -m 2 -o qr/qr-3.png
	cat payloads/payload-4.yaml | qrencode -s 20 -m 2 -o qr/qr-4.png
	cat payloads/payload-5.yaml | qrencode -s 20 -m 2 -o qr/qr-5.png
	cat payloads/payload-6-qr.yaml | qrencode -s 20 -m 2 -o qr/qr-6.png
	convert qr/qr-6.png -set comment "6-f913c615c3a1b24080409b6f9f858aa863f35557432a69e1" qr/qr-6.png
	cat payloads/payload-7.yaml | qrencode -s 20 -m 2 -o qr/qr-7.png
	cat payloads/payload-8.yaml | qrencode -s 20 -m 2 -o qr/qr-8.png

.PHONY: checkpayloads
checkpayloads:
	for i in payloads/*.yaml; do safe_yaml -f $$i; done

.PHONY: nodes
nodes:
	echo "~~~" > nodes/cryptmake.md
	echo "~~~" > nodes/cryptwrap.md
	echo "~~~" > nodes/ketuvim.md
	echo "~~~" > nodes/aesblock.md
	aescrypt -e -p kemmer -o nodes/cryptmake.aes Makefile
	base64 -b 64 -i nodes/cryptmake.aes >> nodes/cryptmake.md
	aescrypt -e -p kemmer -o nodes/cryptwrap.aes nodes/wrap.py
	base64 -b 64 -i nodes/cryptwrap.aes >> nodes/cryptwrap.md
	aescrypt -e -p ketuvim -o nodes/ketuvim.aes stories/qoheleth-3.md
	base64 -b 64 -i nodes/ketuvim.aes >> nodes/ketuvim.md
	cat stories/aesblock.asc >> nodes/aesblock.md
	echo "~~~" >> nodes/cryptmake.md
	echo "~~~" >> nodes/cryptwrap.md
	echo "~~~" >> nodes/ketuvim.md
	echo "~~~" >> nodes/aesblock.md
	cd nodes && python wrap.py *.md

.PHONY: map
map:
	dot -Tpng -o map-labels.png map.dot
	dot -Tpng -N'label=' -o map-nolabels.png map.dot

.PHONY: backup
backup:
	git commit -am "checkpoint"
	tar czvf ~/Dropbox/qoheleth.tgz *

.PHONY: full
full:
	cat stories/qoheleth-{1,2,3,4,5}.md > stories/qoheleth.md
	perl -0777 -i.bak -lne '~s/---\nlayout: post.+?---/Qoheleth (1) Torah\n==================/sm and print' stories/qoheleth.md
	echo "{% include license/cc-by-sa-4.0 author='Madison Scott-Clary' year='2016' %}" >> stories/qoheleth.md
	prose-wc stories/qoheleth.md

include upload.mk

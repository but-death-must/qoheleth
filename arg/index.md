# Qoheleth - a post-self ARG

Qoheleth is a work of fiction in five parts, distributed as an ARG. If you are reading this, then the initial ARG is finished. However, all the assets will remain in place for quite some time, so if you *want* to play, you still can (look for "Qoheleth (1) on post-self.io/entries). Qoheleth was solved on Jan 26, 2017 by [Riismo](http://post-self.io/about/contributors#riismo).

Consider that your spoiler warning.

If you just want to read the story, it's up [here](http://post-self.io/entry/qoheleth).

![Map of Qoheleth](/map-labels.png)

## Mechanics

Here's how Qoheleth worked.

1. There were some teaser tweets, mostly to get the #qoheleth hashtag up and running.
2. Qoheleth (1) was posted on post-self.io with an excerpt that explained that there were eight puzzle pieces out there, with five required to advance. It also included a block of AES-encrypted text. The PR will also include an image and a PGP encrypted block of text.
3. The puzzle pieces mentioned took the form of a split shared secret. When combined using `ssss-combine`, they produce a bit of plaintext.
3. The plaintext is a url to a txti.es site. The site points to a 'node' on some server out there (an EC2 instance). The Node displays a video (Air 'Em Out by clipping.) which includes the lyric "the keyword is kemmer." This is the key to the AES block.
4. The AES block contains a short letter, a SSH private key, and a deck listing, as though a game of cards is being played over email. It also contains the hint that the deck is for Solitaire (also included in the txti.es url, which was /solitaire).
5. While exploring the Archive node server on the EC2 instance, Qoheleth 2 is discovered, a transcription of a recording. The server also includes several other encrypted files. 'kemmer' unlocks all but one, but one of the files it does unlock says that the keyword to the last file is 'ketuvim'.
6. Decrypting that file produces Qoheleth (3), which includes a reference to a node. When that node is visited, an error is produced which suggests the user check the Gist catalog.
7. Visiting that node on gist.github.com shows Qoheleth (4). It includes a reference to a node on the Archive with a block of alphabetical cypher text and a gist with a means to decrypt it (via solitaire algo).
8. The deck from #4 unlocks the solitaire block, which reveals the username for SSHing to the server using the key from #4 and the passphrase for a private key.
9. SSHing to the Archive server dumps the private key for the blob in #2. Decrypting the blob with the key and the passphrase from #8 produces Qoheleth (5).
10. The story includes instructions for notifying the author of success by showing the contents of Qoheleth (5) and all of the keys required (kemmer, ketuvim, Nevi'im, and the solitaire key).
11. All five chapters will be posted, and a link to this repository will go up in a news item, with another spoiler warning for others who want to go through the game. Encrypted blocks will remain encrypted and node references will be obfuscated.

## Questions:

Should I do this through an anonymous user? Some of the stuff is pretty easily traced back to me, but maybe that's unimportant. If so, need a few things:

* Throw-away email account
* Throw-away GitHub account
* Throw-away reddit account (dissemination + imgur)
* Server (droplet? EC2 instance?) for logging in and serving anonymous pages

One neat thing to do is to use the throw away usernames as keys, maybe.

## Plot points:

* The other Odist: "Life breeds life, but death must now be chosen." (early in ode, used to generate usernames)
* Dear's parent: "Dear the wheat and rye under the stars"
* Dear's sibling: "Serene; sustained and sustaining."
* Dear: "Dear, also, the tree that was felled"
* Dear's first long-lived fork: "Which offered heat and warmth in fire."
* first line in Dear's stanza: "Those that lived, providing life in death, are forever praiseworthy."

The ode is Ode To The End Of Death. The original upload didn't write the ode, but co-opted the un-published poem from a dead friend; the names stand in memoriam. No Odist will tell the name of the friend, and some have investigated burning that name from their minds.

The plot of the two stories is that there are rumors of one of the clade sharing The Name, but it's proving hard to verify. A search (like the ARG) is setup to hunt down who and why. Turns out to be the upload, assassinated by a Guo Wei instance by Life, leaving nothing left to merge.

## Resources

ec2 instance: 35.165.134.227

Usernames
* life.breeds.life@gmail.com (used to log in to imgur via G+, user hebelqoheleth.imgur.com)
* github.com/but-death-must
* reddit.com/user/now-be-chosen

txties: http://txti.es/solitaire  

Shares:

    1-bb691b959d0e82c2c14aa3d942d0d5a2c04ace8458c5ab67 with first PR in posts/ (QR)
    2-5b7d05093625f975ac19afa7ab21bffe6974f20a9ac3d2e4 tumblr (QR) https://tmblr.co/ZZIuve2GtJilu
    3-07d6d22cb0b0012bec96c25d172100a5136941a2bbdd20c6 twitter (json)
    4-d9f0aa3b9f9f8df1fbde586ba9efed6ee3ddc432e185e1b2 GitHub icon (QR)
    5-0e90e1933675e1987690abeecb663c75573b7da40009ed9b physical (QR)
    6-f913c615c3a1b24080409b6f9f858aa863f35557432a69e1 imgur stego (QR)
    7-76eb0989083434f8222381950f39941e4e5d59a5544df784 on EC2 instance, link in story (yaml)
    8-d654bf5fd82236a0b27d42794b83a21e141469616d9c7f81 as metadata on story (yaml)

Solitaire impl: ~~https://github.com/but-death-must/cards~~ https://github.com/makyo/cards via https://gist.github.com/but-death-must/0fedcbbb5e9839936ce799ece39fcd49

Solitaire key: ♦2 ♠8 ♠Q ♦8 ♣9 ♣Q ♥2 ♦A ♦4 ♣4 ♣3 ♣A ♠J ♣2 ♦7 ♦5 ♠7 ♥9 ♥5 ♠10 ♥7 AX ♥10 ♠3 ♥4 ♣8 ♠9 ♣6 ♠4 ♥J ♥K ♣10 ♦J BX ♣5 ♣K ♣J ♥8 ♥3 ♦9 ♠2 ♠A ♥Q ♥A ♥6 ♦K ♠5 ♣7 ♦Q ♦10 ♠6 ♦6 ♦3 ♠K

Plaintext: server three five dot one six five dot one three four dot two two seven stop username quote qoheleth quote lower case stop normal key stop passphrase for key you receive is quote nevi apostrophe im quote title case one word end message

Copypasta:
♦2 ♠8 ♠Q ♦8 ♣9 ♣Q ♥2 ♦A ♦4 ♣4 ♣3 ♣A ♠J ♣2 ♦7 ♦5 ♠7 ♥9 ♥5 ♠10 ♥7 AX ♥10 ♠3 ♥4 ♣8 ♠9 ♣6 ♠4 ♥J ♥K ♣10 ♦J BX ♣5 ♣K ♣J ♥8 ♥3 ♦9 ♠2 ♠A ♥Q ♥A ♥6 ♦K ♠5 ♣7 ♦Q ♦10 ♠6 ♦6 ♦3 ♠K
server three five dot one six five dot one three four dot two two seven stop username quote qoheleth quote lower case stop normal key stop passphrase for key you receive is quote nevi apostrophe im quote title case one word end message

Cyphertext:
OCYNX GRIMN CYJPE PNNXS SCIQZ
KTWQW FBAVY FBOPA QERLB HWIJW
KPELO UCLAN OKHPM PCPWR NZNZQ
NMTIQ BKNGH UWFMG BPPZS CNRKX
TKEMU AFNOS VQUNW

Copypasta:
♦2 ♠8 ♠Q ♦8 ♣9 ♣Q ♥2 ♦A ♦4 ♣4 ♣3 ♣A ♠J ♣2 ♦7 ♦5 ♠7 ♥9 ♥5 ♠10 ♥7 AX ♥10 ♠3 ♥4 ♣8 ♠9 ♣6 ♠4 ♥J ♥K ♣10 ♦J BX ♣5 ♣K ♣J ♥8 ♥3 ♦9 ♠2 ♠A ♥Q ♥A ♥6 ♦K ♠5 ♣7 ♦Q ♦10 ♠6 ♦6 ♦3 ♠K
OCYNX GRIMN CYJPE PNNXS SCIQZ KTWQW FBAVY FBOPA QERLB HWIJW KPELO UCLAN OKHPM PCPWR NZNZQ NMTIQ BKNGH UWFMG BPPZS CNRKX TKEMU AFNOS VQUNW

ssh message:

```
You've gotten this far :)

You're welcome at any time.

Bring everyone.

-----BEGIN PGP PRIVATE KEY BLOCK-----
```

35.165.134.227/node/c4ef31fd9d5849e527c272f6d65374af0670aab1/

TODO: More story embedded in clues

-----
It's underway now. Things have shifted from above, but all that remains is to finish writing parts 3, 4, and 5, and create the PR.
-----
## Marketing:

All queries respond with:

הֲבֵל הֲבָלִים

havel havalim

הֲבֵל הֲבָלִים אָמַר קֹהֶלֶת הֲבֵל הֲבָלִים הַכֹּל הָבֶל
havél havalím 'amár kohélet havél havalím hakól hável.
Vanity of vanities, saith Koheleth; vanity of vanities, all is vanity.

Give each step a month before reveling a key.

### tweets

\#qoheleth [map.png]

\#qoheleth Fingerprint=C4EF 31FD 9D58 49E5 27C2  72F6 D653 74AF 0670 AAB1

DEAR: So, one of us did a pretty exhaustive search of some records and found some old archive server running somewhere. #qoheleth

"We could. Some of us probably already have. I want the key, though. It's probably a word or something and may prove interesting." #qoheleth

"Mmhm. Finally decided to explore relationships," it said. "They accuse me of treating it like an art project" #qoheleth

Dear turned back around. Its arms were held tight against it's front though whether from cold or emotion, Ioan couldn't tell. #qoheleth

Dear's lovely, and it's totally right: on the other side of the clade, there are some who'd not like this kind of digging. #qoheleth

\#qoheleth [screen shot of file listing]

Forking and mutating, forking and mutating. You can change your form easily enough, but it's much harder to change your sensorium. #qoheleth

I know I'm gone, I'm a lost cause, but much of the clade still has their faculties about them. #qoheleth

There are three parts to the Tanakh, I'm told. The Torah, or teachings; the Nevi'im, or Prophets; and the Ketuvim, or writings. #qoheleth

### thunderclap

I have a quick request! I need as many people to tweet (not retweet) `#qoheleth {"payload-micro":{"share":"3-07d6d22cb0b0012bec96c25d172100a5136941a2bbdd20c6","scheme":"(5,8)","next":"Software"}} <link to @post_self tweet for first story>` as possible.

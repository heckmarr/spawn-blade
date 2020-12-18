#!/bin/fish
/usr/bin/codium & 
terminator -T 'Local Sync' --geometry=700x350+3122+700 --profile=candy-fluff  & 
terminator -T 'Local Build' --geometry=600x350+1922+700  --profile=candy-fluff & 
terminator -T 'Remote Root' --geometry=300x350+2521+700 --profile=oo & 
terminator  -T 'Remote Unpriviledged' --geometry=300x350+2822+700 --profile=oo &
#terminator -T 'mouse' --geometry=50x10+1922+0 --profile=doink &
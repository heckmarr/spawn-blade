#!/usr/bin/env bash
/bin/firefox
terminator -T 'Local Sync' --geometry=700x350+1202+700 --profile=candy-fluff  &> /dev/null
terminator -T 'Local Build' --geometry=600x350+2+700  --profile=candy-fluff &> /dev/null
terminator -T 'Hamstercam' --geometry=300x350+601+700 --profile=verysmol &> /dev/null
terminator  -T 'Remote Unpriviledged' --geometry=300x350+902+700 --profile=oo &> /dev/null


install: requirement.txt
	pip install -r requirement.txt

ROUND=50
SEQ := 1 2 3 4 5

# ROUND set to 0 for infinite test
# 1 -> test_web_browser
# 2 -> test_video_play
# 3 -> airplane mode
# 4 -> wifi 
# 5 -> data 

run:
	python testing.py --device Android:// --log $(shell date +'%Y%m%d-%H%M').log -r $(ROUND) -s $(SEQ)

rand:
	python testing.py --device Android:// --log $(shell date +'%Y%m%d-%H%M').log -r $(ROUND)

DEBUG=10
INFO=20
WARN=30
ERROR=40
FATAL=50

test:
	python testing.py --device Android:// --log test.log --level $(DEBUG) -r 1 -s $(SEQ)
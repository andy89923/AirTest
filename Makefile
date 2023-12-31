
install: requirement.txt
	pip install wheel
	pip install -r requirement.txt

ROUND=50
SEQ := 1 2 3 4 5
NETWORK=DATA

# ROUND set to 0 for infinite test
# 1 -> test_web_browser
# 2 -> test_video_play
# 3 -> airplane mode
# 4 -> wifi 
# 5 -> data 

run:
	python testing.py --device Android:// --log log/$(shell date +'%Y%m%d-%H%M').log -r $(ROUND) -s $(SEQ) -d $(NETWORK)

rand:
	python testing.py --device Android:// --log log/$(shell date +'%Y%m%d-%H%M').log -r $(ROUND) -d $(NETWORK)

DEBUG=10
INFO=20
WARN=30
ERROR=40
FATAL=50

test:
	python testing.py --device Android:// --log log/test.log --level $(DEBUG) -r 1 -s $(SEQ) -d $(NETWORK)
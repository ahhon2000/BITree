.PHONY: nothing test

nothing:
	echo 'did nothing' $(REMOTE_SERVER)

test:
	tests/test

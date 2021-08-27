CC := gcc
# CFLAGS := -Wall -Wextra -Werror -Wno-unused-parameter -Wno-unused-function -g
SOURCES = $(wildcard *.c)
EXCES = $(SOURCES:%.c=%.o)
DEPS = $(wildcard *.h)

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

all: $(EXCES)
	$(CC) $(CFLAGS) -o murakumo main.o hash_table.o

clean:
	rm -rf hash_table.o main.o murakumo
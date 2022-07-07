CC=gcc-11
CFLAGS = -I.
LDFLAGS = -std=c11


SRCS = $(wildcard *.c)

OBJDIR = .build


OBJS = $(SRCS:%.c=$(OBJDIR)/%.o)

TARGET = tic-tac-toe

.PHONY: clean $(TARGET)


$(OBJDIR)/%.o : %.c | $(OBJDIR)
	@echo [CC] $@
	@$(CC) $(LDFLAGS) $(CFLAGS) -c $<  -o $@


$(TARGET) : $(OBJS)
	@echo [LL] $@
	@$(CC) $(LDFLAGS) -o $(TARGET) $^


clean:
	@echo [CLEAN DONE!!]
	@rm -rf $(OBJDIR) $(TARGET)


$(OBJDIR):
	@mkdir -p $@



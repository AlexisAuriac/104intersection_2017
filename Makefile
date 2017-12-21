##
## EPITECH PROJECT, 2017
## 104intersection
## File description:
## Makefile for 104intersection.
##

NAME	=	104intersection

all	:	$(NAME)

$(NAME)	:	intersection.py
		cp intersection.py $(NAME)

fclean	:
		rm -f $(NAME)

.PHONY	:	all	fclean

##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## 301dannon Makefile
##

SRC	=	src/main.py

NAME	=	302separation

all:	$(NAME)

$(NAME):
		ln -s $(SRC) $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf $(NAME)

fclean:	clean

re:	fclean all

.PHONY: all $(NAME) clean fclean re

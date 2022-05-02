
- **Choosed language:** python
- **Compilation:** via Makefile, including re, clean and fclean rules

# Subject
    Starting with a file that contains a list of friendship links between different Facebook accounts, the goal of
    this project is to use graph theory to compute the degree of separation between two people.
        Your program must display the following:
            • the list of people in alphabetical order (the order that will be used to build the matrices),
            • the adjacency matrix,
            • the matrix of the shortest paths, with lengths less than or equal to n.
        If two names are given as argument to the program, it must instead display the degree of separation between those two people, or -1 if they are not connected.
## Prerequisites

What you need

```
python3
make
```

## Compiling

Clone the repository and go inside. Then,

```
$ make
```

## Usage

```
    USAGE
        ./302separation file [n | p1 p2]
    DESCRIPTION
        file file that contains the list of Facebook connections
        n maximum length of the paths
        pi name of someone in the file

```

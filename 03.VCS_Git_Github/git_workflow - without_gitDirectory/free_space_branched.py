#!/usr/bin/env python3

def main():
    '''
    git branch ----> lists all branches
    git branch <branch_name> ----> creates a new branch
    git checkout <branch_name> ----> switches to a branch
    git checkout -b <branch_name> ----> creates a new branch and switches to it
    git branch -d <branch_name> ----> deletes a branch
    git merge <branch_name> ----> merges a branch into the current branch
    '''
    '''
    just keep the change to resolve conflict

    << << << < HEAD
    # commented on master
    == == == =
    # comment on second_one branch
    >>>>>> > second_one
    '''
    pass


main()

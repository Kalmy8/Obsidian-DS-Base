
#### git checkout

So, `git checkout` has two main personalities:

1.  **Branch Management**: `git checkout <branch_name>`
    *   Switches your `HEAD` to point to a different branch, updating your entire working directory to match.
2.  **File Management**: `git checkout [<commit_or_branch>] -- <file_path(s)>`
    *   "Checks out" files from a source (a commit, a branch, or the staging area) and places them into your working directory. It does **not** switch your branch.

##### 2. Discarding Changes in Multiple Files

You can list as many files as you want to discard their changes:

```bash
# Discard changes in file1.txt and path/to/file2.py
git checkout -- file1.txt path/to/file2.py
```

##### 3. Discarding Changes in an Entire Directory

To discard all unstaged changes in a specific directory and all its subdirectories, just provide the path to the directory:

```bash
# Discard all changes in the 'src/components' directory
git checkout -- src/components/
```

And as you saw before, using `.` discards all changes in the entire project:

```bash
# Discard all unstaged changes in the current directory and subdirectories
git checkout -- .
```

##### 4. Getting a File from Another Branch

This is a really powerful feature. You can pull a specific file from another branch into your current working directory without switching your entire branch. This is great for when you just need one or two files from a feature branch.

```bash
# Bring the version of 'config.json' from the 'develop' branch into your current branch
git checkout develop -- config.json
```

After running this, `config.json` in your working directory will be identical to the one in the `develop` branch. You can then stage and commit it as usual.

##### 5. Getting a File from a Specific Commit

You can even go back in time and grab a version of a file from a specific commit hash:

```bash
# Restore the version of 'main.py' from commit a1b2c3d
git checkout a1b2c3d -- main.py
```

This is incredibly useful for reverting a specific change in one file without having to revert an entire commit.


#### git config 

Задает имя и почту пользователя, **от лица которого будут совершаться комиты**

![[Pasted image 20251026223322.png]]

#### git tag

tag is a pointer to a specific commit. Tags are divided in 2 categories:
1. **"Lightweight" tag**, only has a name and a hash. Can be created with `git tag` command
2. **"Annotated" tag,** has a name, a hash, author ID an message
![[Pasted image 20251026224457.png]]

**Tags are not pushed to the remote automatically**
![[Pasted image 20251026224508.png]]

#### Detached Head
- Head is a pointer which shows you what is your current working tree state (what branch are you on? what "commit" does your current working tree represent?)
- Use it to observe files made earlier
- If you want to actually make some changes - you create a new git branch from that elder commit first, checkout to that branch and then start changing files

#### "Dangling" commits

- "Dangling" commits occur when you delete an unmerged branch
- Commits from that branch become "dangling" and will eventually be deleted by a garbage collector
- You can restore those commits by creating  a new branch of them. "Dangling" commits hashes can be observed with git `reflog` command
![[Pasted image 20251026225722.png]]


#### Merging

- Main instrument to bring changes from one git branch into another one
- After a merge, commit actually becomes a part of both branches
![[Pasted image 20251026230051.png]]**There are 4 types of merges:**![[Pasted image 20251026230131.png]]

##### Fast-forward (FF) merge
![[Pasted image 20251026230627.png]]
- Simply includes commits from one branch into another branch
- **Is only possible if no other commits was made on the branch we merge onto (e.g. master in the example below)**
- Preserves linear history
- **Do not forget to delete a feature branch after, otherwise there will be dozens of them**
	- If you want to preserve "the history" - include that information about the feature branch inside the commit message or make a tag

##### Merge commit
![[Pasted image 20251026231151.png]]
- Is usually used when branches both branches had some changes after diverging
- As the result, **a new merge commit is created** 
- **Even if branches are fast-forwardable, you still can explicitly tell git to create a merge commit** (some team's policy)
![[Pasted image 20251026231131.png]]
- If branches had different changes on the same file - **merge commits might occur**

###### Merge conflicts

- Occure when a single file 
![[Pasted image 20251026232125.png]]
- Git is smart enough to automatically merge changes to different parts of a single file:
![[Pasted image 20251026232051.png]]

- Merge conflicts occure less when you do a frequent and small changes
	- In some degree we could say that modular, decoupled code is easier to merge, so **the presence of merge conflicts can highlight code-quality issues**
- ![[Pasted image 20251026232324.png]]

![[Pasted image 20251026232828.png]]

#### Rebasing 

![[Pasted image 20251026233246.png]]


![[Pasted image 20251026233315.png]]
![[Pasted image 20251026233413.png]]
![[Pasted image 20251026233540.png]]
![[Pasted image 20251026233709.png]]

### Merge vs. Rebase: What Happens to the Commits?

A common point of confusion is what happens to the commits and the branches during these operations.

**With `git merge`:**
- A merge operation, especially one creating a merge commit, ties two histories together. That merge commit has two parents, linking it to both branches. After merging `develop` into `main`, the `main` branch now contains all the work from `develop`.

**With `git rebase` (e.g., `git rebase main` while on `develop`):**
- **Commits are not shared; they are copied.** Rebasing takes the unique commits from your current branch (`develop`), creates new commits with the same changes, and applies them on top of the target branch's (`main`) last commit. The original commits on `develop` are discarded.
- **The target branch (`main`) is not changed at all.** It remains exactly where it was.
- **Your current branch (`develop`) is updated.** Its pointer is moved to the end of this new chain of commits.
- **You still need to merge.** After the rebase, `main` does not have the new commits from `develop`. You still need to merge the updated `develop` branch into `main`. However, this merge will now be a simple fast-forward, creating the clean, linear history that is the goal of rebasing.

**1. Why and when to use `checkout featureX` then `rebase main`?**

This is the primary and most recommended use case for `git rebase`. You do this to incorporate the latest changes from `main` into your `featureX` branch. This is important before you merge your feature branch back into `main`.

- **Why?** It maintains a clean, linear project history. Instead of a merge commit that brings two histories together, rebasing makes it look like you created your feature branch from the very latest point on `main`.
- **When?** Frequently during the development of a feature, and always right before creating a pull request to merge `featureX` into `main`.

#### git stash

- Use `git stash` when you want to record the current state of the working directory and the index, but want to go back to a clean working directory.
- The command saves your local modifications away and reverts the working directory to match the `HEAD` commit.
- The modifications stashed away can be listed with `git stash list`, inspected with `git stash show`, and restored (potentially on top of a different commit) with `git stash apply`.

**Common commands:**
- `git stash`: Stash the changes in a dirty working directory away.
- `git stash list`: List all stashed changes.
- `git stash pop`: Apply the topmost stash, and remove it from the list.
- `git stash apply`: Apply the topmost stash, but leave it in the stash list.
- `git stash drop`: Remove a single stashed state from the stash list.
- `git stash clear`: Remove all stashed states.

#### git cherry-pick

- `git cherry-pick <commit-hash>` is used to apply a specific commit from one branch to another.
- It is useful for when you don't want to merge an entire branch, but only need to include one or two specific commits.
- For example, if you have a bug fix on a feature branch that is not ready to be merged, you can cherry-pick that commit and apply it to your `main` or `develop` branch.
- This creates a *new* commit on the target branch with the same changes. The new commit will have a different hash.

#### Rewriting history
ONLY IF YOU DID NOT SHARE THE HISTORY ALREADY (#TODO what does that mean?)

##### Amend
![[Pasted image 20251026233821.png]]

##### Interactive rebase

![[Pasted image 20251026233954.png]]


![[Pasted image 20251026234208.png]]

![[Pasted image 20251026234606.png]]






**2. What does it mean to "not change git history if it's already shared"?**

When you use commands that rewrite history (like `rebase` or `commit --amend`), you are creating *new* commits and removing the old ones from the branch's history.

- **Shared History:** If you have pushed your branch to a remote repository (like GitHub), other developers may have pulled your branch and started building their own work on top of your commits. Your history is now "shared".
- **The Problem:** If you then rewrite your history and force-push the changes, you have created a new history. Your teammates are still holding onto the old history. When they try to pull the new changes, Git will see two diverged histories, leading to confusion, complex merges, and potentially lost work.
- **The Rule:** As a rule of thumb, it is safe to rewrite history that only exists on your local machine. Once you `git push`, you should avoid rewriting that history.

### Exception: Rebasing Your Own Feature Branch

The rule above has a crucial exception. It's perfectly normal and expected to rebase your **own personal feature branch**, even after you have pushed it to the remote. A branch like `feature/alexey-fixes-bug` is considered "owned" by you.

- **Why is it safe?** The team agreement is that no one else should be branching off of your personal feature branch. You are free to clean it up and rewrite its history.
- **How do you do it?** After you rebase your local branch against `main`, the history will diverge from the remote version of your branch. You must then use `git push --force-with-lease` to update the remote. This is a safer version of `force push` that won't overwrite any work if someone else *did* happen to push to your branch.

### What About Large, Collaboratively Developed Features?

If multiple developers need to work on a single large feature branch (`feature/new-checkout-flow`), that branch effectively becomes a **shared branch**.

- **You can no longer rebase this branch.** It has the same status as `main` or `develop`. Rebasing it would break things for everyone collaborating on it.
- **To keep it updated, you must merge `main` into it.** Periodically, one person should run `git merge main` on the feature branch. This creates a merge commit, but it safely brings in the latest updates without rewriting history.
- **Sub-branches:** Developers can then safely create sub-branches from this shared feature branch and use `rebase` on their *own* sub-branches to keep them in sync with the main feature branch.







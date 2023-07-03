#!/usr/bin/python3

"""
Module: 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Track visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not visited[key]:
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add the box to the stack

    return all(visited)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))


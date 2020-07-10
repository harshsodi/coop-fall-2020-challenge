class EventSourcer():
    # Do not change the signature of any functions

    """
    Use a list to store actions.
    The action states only what to add to current value. Negative for subtract operation
    Keep moving ahead on add or subtract and accordingly for undo and redo
    """

    def __init__(self):
        self.value = 0

        # State tracking variables
        self.history = [0] # Timeline to keep track of actions performed. history[i]=x -> action "add x"
        self.current_action_pointer = 0 # The current point in the timeline

    def perform_action(self, action=1):
        """
        Perform the action that is pointed by the current_action_pointer

        action: To determine whether to perform the action or to reverse it
            1 -> perform
            -1 -> Reverse the action
        """
        self.value += self.history[self.current_action_pointer] * action

    def add(self, num: int):
        """
        Add the given "num" to the current value
        """

        # Add the action to the timeline
        if self.current_action_pointer == len(self.history) - 1: 
            # If we are at the most recent point, extend the timeline
            self.history.append(num)
        else:
            # Update the next step in the timeline
            self.history[self.current_action_pointer + 1] = num

        self.current_action_pointer += 1 # Point to the recently added action
        self.perform_action() # Perform that action

    def subtract(self, num: int):
        """
        To subtract the given numebr "num" from current value 
        """
        self.add(-num)

    def undo(self):
        """
        Move one step back in the timeline
        """
        self.bulk_undo(1)

    def redo(self):
        """
        Move one step ahead in timeline
        """
        self.bulk_redo(1)

    def bulk_undo(self, steps: int):
        """
        Undo the current action and move the pointer to previous step, "steps" times
        """

        for i in range(steps):
            self.perform_action(-1)
            self.current_action_pointer -= 1

            # If the end is reached, not possible to move back anymore. Exit
            if self.current_action_pointer == 0:
                break

    def bulk_redo(self, steps: int):
        """
        Move the pointer to the next action and perform the action, "steps" time
        """

        for i in range(steps):
            self.current_action_pointer += 1

            # If the far end is reached, can't move any further. Exit
            if self.current_action_pointer == len(self.history):
                break

            self.perform_action()
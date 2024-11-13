#1. A dictionary storing each conversation as keys and the value being
#a list (or deque) of messages. This would allow for O(1) access to each conversation, and 
#O(1) access to the first or last message if its a deque. However, when using an array,
#linked-list, or deque, searching for any message but the first or last would take
#O(n) time. For the most efficient search, a Binary Tree allows for O(log n)
#search complexity.

#2. Using some sort of linked-list or queue seems best for quickly
#rendering the most recent message without incurring too much storage
#overhead. Polling is where the client send requests to the server at regular
#intervals, and the server responds when it has new information. Long-polling
#is when the client sends a request and the connection is kept open until 
#there new information tot deliver, whereupon he request is closed and
#then reopened. Websockets maintains a constant connection, which allows for
#immediate communication, but also consumes more resources than he first
#two options. 

#3. An aarray, while simple to implement, would not allow for efficient
#searching and retrieval of messages. Using a hash table to index conversations,
#and having each conversation stored as a linked list would allow for O(1) 
#searching of conversations, and new messages in a conversation will move it to 
#the front. A tree would provide similar functionality (older messages more accessible,
#newer ones less so) for a similar memory cost.

#Part 2

#1. In this algorithm, we are iterating over every element in array n, and for each
#element, we are iterating through the list again to see if each element is greater
#than the next consecuive element, and if it is, teir values are switched.

#2. Iterating through the list once would be O(n), and since we're iterating again
#for each element, it would be O(n)*O(n) = O(n^2)

#3. To improve the algorithm, we can check to see if a swap has occurred in each
#pass to prevent unnecessary loops after the list is sorted. We could also adjust it
#so that the loop moves in both directions at the same time.
'''
(* *) Realisiert eine double ended queue (DEQueue), welche es ermöglicht an beiden Enden einer Queue zu lesen und zu schreiben. 
Um beides effizient zu ermöglichen, soll die DEQueue als doppelt verkettete Liste realisiert werden. Das bedeutet, 
dass jedes Element nicht nur auf den nächsten Eintrag zeigt, sondern auch auf den vorherigen. Eure DEQueue soll die folgenden Operationen anbieten:

enqueue(self, value), Hinzufügen, wie bei einer Queue
dequeue(self), Entfernen, wie bei einer Queue
unenqueue(self), Entfernen des zuletzt mittels enqueue hinzugefügten Wertes
undequeue(self, value), Hinzufügen eines Wertes, welcher als nächstest mittels dequeue entfernt werden kann
front(self), Lesen des Wertes, welcher mittels dequeue entfernt würde
back(self), Lesen des Wertes, welcher zuletzt mittels enqueue hinzugefügt wurde

Implementiert eine solche DEQueue als doppelt verkettete Liste. Achtet darauf, dass an beiden Enden gelesen und geschrieben werden kann und alle 
Lese- und Schreiboperationen konstante Laufzeit haben. Die Implementierung soll unter Verwendung von Klassen und Objekten erfolgen.


'''
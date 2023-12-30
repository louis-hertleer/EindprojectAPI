# API

In mijn vrije tijd doe ik graag landbouw activiteiten, daarom heb ik voor mijn api iets in dit thema gekozen.
De database bestaat uit 3 tabellen waarbij een worker een tractor en een location kan hebben.
Een worker heeft een: id,email, een hashed_password en een list van tractors/locations.
Een tractor heeft:id, type, year, worker_id.
Een Location heeft: id, type, address, worker_id.

De location is een uitbreiding op de eerste versie van mijn API.
In deze versie van mijn API is er ook authentication en de passwords zijn gehashed.
Er zijn ook enkele endpoints bijgekomen.






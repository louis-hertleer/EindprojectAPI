# API

In mijn vrije tijd doe ik graag landbouw activiteiten, daarom heb ik voor mijn api iets in dit thema gekozen.
De database bestaat uit 3 tabellen waarbij een worker een tractor en een location kan hebben.
Een worker heeft een: id,email, een hashed_password en een list van tractors/locations.
Een tractor heeft:id, type, year, worker_id.
Een Location heeft: id, type, address, worker_id.

De location is een uitbreiding op de eerste versie van mijn API.
In deze versie van mijn API is er ook authentication en de passwords zijn gehashed.
Er zijn ook enkele endpoints bijgekomen.


De eerste request die gemaakt moet worden is een worker aanmaken(POST):
![Create Worker](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/2afc9a6e-dce4-4d31-a5e3-803c0b597dee)

Er kan ook een tractor gemaakt worden voor een worker(POST):
![Create Tractor For worker](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/cb557145-3ace-4637-9e2d-c377620d8f5a)

Ook kan er een location gemaakt worden voor een worker(POST):
![Create Location For worker](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/240ab964-dc49-45da-9046-396f3f564858)

Om te authenticeren kan een token opgevraagd worden(POST):
![Get Token POST](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/4e1f4180-5f3d-4eb1-8aaa-67cc4693bb4b)

Om GET requests te maken moet de user ingelogd zijn.
Alle workers kunnen kunnen samen met hun tractors en locations opgevraagd worden(GET):
![Get Workers](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/40278be8-d63e-42b9-9200-70f7b7252d51)

Een worker kan opgevraagd worden per ID samen met hun tractors en locations(GET):
![Get Worker with ID](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/92568059-7df4-41a7-a2b9-bf79a8f59a4a)

Alle tractors kunnen worden opgevraagd(GET):
![Get Tractors](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/2f5f79bc-6ffd-4f90-baa6-fea414a29ef1)

Alle locations kunnen worden opgeraagd(GET):
![Get Locations](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/7ce866c8-c3e6-45ba-9d14-ef90339d6a6e)

Een tractor kan verwijdered worden(DEL):
![Delete Tractor](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/d2acbc7f-3f83-4570-91db-27c6df60bd84)

Een location van een user kan aangepast worden(PUT):
![Update workers location](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/c02c041c-8000-454a-a823-5f4b95a2dd36)

Als een user niet geauthenticeerd is kan hij geen GET requests maken:
![NotAuthenticated](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/7d4ba4bb-a437-4ff0-94b5-5c3296e854ba)

Hier is de volledige OpenAPI docs pagina:
![OpenAPI docs](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/d3c5db3a-4a6e-491b-8964-902d986a9ea1)

Hier is een bewijs dat OpenAPI docs pagina ook werkt:
![OpenAPI Proof](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/4a9b55f4-6f8d-4c7b-a50f-58af6b76da23)

Alle test werken via pytest:
![Test](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/12e5c52e-de9b-408f-9781-932720fb4f81)

Als laatste een bewijs dat de API volledig werkt via Okteto cloud:
![HostedSS](https://github.com/louis-hertleer/EindprojectAPI/assets/114073936/3e097fdf-8337-4841-ba15-6c6801b9466e)

De API is hier gehost: https://system-service-louis-hertleer.cloud.okteto.net

username/email: Example@gmail.com
password: admin
Token voor postman: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJFeGFtcGxlQGdtYWlsLmNvbSIsImV4cCI6MTcwMzc5Mzc0OH0.mQzAilWEWPwX5pCfXS5_hXsJmUTnd8g0q3Ye_Sxyu1I



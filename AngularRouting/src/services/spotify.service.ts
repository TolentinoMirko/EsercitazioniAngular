import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root'
})
export class SpotifyService {

 constructor(private http: HttpClient) { }

 searchTrack(query: string) {
   const url = `https://api.spotify.com/v1/search?q=${query}&type=track`;
   
   const headers = new HttpHeaders({Authorization: environment.oauthToken});

   let obsTracks = this.http.get(url, { headers });
   return obsTracks;

 }

 getTrack(id: string) {
  const url = `https://api.spotify.com/v1/tracks/${id}`;
  const headers = new HttpHeaders({Authorization: environment.oauthToken});
  
  return this.http.get(url, { headers });
  //questo return serve per fare la richiesta alla api di spotify dandogli l'url e l'autenticazione
}

} 




import { Injectable } from "@angular/core";
import { Http, Response } from "@angular/http";
import { Observable } from "rxjs/Observable";
import "rxjs/add/observable/throw";
import "rxjs/add/operator/map";
import "rxjs/add/operator/catch";
import { Note } from "./models";
import { AppSettings } from "../app.settings";


@Injectable()
export class NoteService {
    constructor(private http: Http) {
    }

    private getNotesUrl = 'api/v1/notes/list/';

    getNotes(): Observable<Note[]> {
        return this.http.get(`${AppSettings.BACKEND_URL}/` + this.getNotesUrl)
            .map(this.extractData)
            .catch(this.handleError);
    }

    private extractData(res: Response) {
        let body = res.json();
        // console.log(body);
        return body || {};
    }

    private handleError(error: any) {
        let errMsg = (error.message) ? error.message :
            error.status ? `${error.status} - ${error.statusText}` : 'Server error';
        console.error(errMsg);
        return Observable.throw(errMsg);
    }
}
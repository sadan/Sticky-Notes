import { Component } from "@angular/core";
import { ROUTER_DIRECTIVES } from "@angular/router";
import { NoteService } from "../notes/notes.service";
// import './rxjs-operators';


@Component({
    moduleId: module.id,
    selector: 'my-app',
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.css'],
    directives: [ROUTER_DIRECTIVES],
    providers: [NoteService]
})
export class HomeComponent {

}
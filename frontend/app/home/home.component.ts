import { Component } from "@angular/core";
import { ROUTER_DIRECTIVES } from "@angular/router";
import { NoteService } from "../notes/notes.service";


@Component({
    moduleId: module.id,
    selector: 'sn-app',
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.css'],
    directives: [ROUTER_DIRECTIVES],
    providers: [NoteService]
})
export class HomeComponent {

}
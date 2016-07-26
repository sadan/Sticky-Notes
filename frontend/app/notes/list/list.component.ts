import { Component, OnInit } from '@angular/core';

import { Note } from "../models";
import { NoteService } from "../notes.service";
import { CreateNoteComponent } from "../create/create.component";


@Component({
    moduleId: module.id,
    selector: 'sn-notes',
    templateUrl: 'list.component.html',
    styleUrls: ['list.component.css'],
    directives: [CreateNoteComponent]
})
export class NotesListComponent implements OnInit {
    notes: Note[];
    errorMessage: any;
    
    constructor(private noteService: NoteService) {
    }

    getNotes() {
        this.noteService.getNotes()
                        .subscribe(
                            notes => this.notes = notes,
                            error => this.errorMessage = <any>error
                        );
    }

    ngOnInit() {
        this.getNotes();
    }
}
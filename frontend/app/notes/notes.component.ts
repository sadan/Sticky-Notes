import { Component, OnInit } from '@angular/core';
import { NewNoteComponent } from './new-note.component';

import { NoteService } from './notes.service'
import { Note } from "./note";


@Component({
    moduleId: module.id,
    selector: 'my-notes',
    templateUrl: 'notes.component.html',
    styleUrls: ['notes.component.css'],
    directives: [NewNoteComponent]
})
export class NotesComponent implements OnInit {
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
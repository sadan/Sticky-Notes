import { provideRouter, RouterConfig } from "@angular/router";
import { NotesComponent } from "../notes/notes.component";

const routes: RouterConfig = [
    {
        path: '',
        redirectTo: '/notes',
        pathMatch: 'full'
    },
    {
        path: 'notes',
        component: NotesComponent
    }
];

export const appRouterProviders = [
    provideRouter(routes)
];
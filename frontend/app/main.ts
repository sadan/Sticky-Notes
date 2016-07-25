import { bootstrap } from "@angular/platform-browser-dynamic";
import { disableDeprecatedForms, provideForms } from '@angular/forms';
import { HTTP_PROVIDERS } from '@angular/http';

import { HomeComponent } from "./home/home.component";
import { appRouterProviders } from "./home/home.routes";

bootstrap(HomeComponent, [
    disableDeprecatedForms(),
    provideForms(),
    HTTP_PROVIDERS,

    appRouterProviders
]);
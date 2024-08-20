import { ValidatorFn, AbstractControl } from '@angular/forms';

export class XcvValidator {


}

export function DomainValidator(): ValidatorFn {
  return (control: AbstractControl) => {
    // const regex = /^(((?!(www\.))(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\-\_]{0,48}[a-zA-Z0-9]))\.){0,126}(?!(www\.))(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\-]{0,48}[a-zA-Z0-9]))\.(([a-zA-Z0-9]{2,12}\.[a-zA-Z0-9]{2,12})|([a-zA-Z0-9]{2,25})))$/;
    // const regex = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/i; // Regular expression for URL validation
    // const regex = /^(?![^\n]*\.$)(?:https?:\/\/)?(?:(?:[2][1-4]\d|25[1-5]|1\d{2}|[1-9]\d|[1-9])(?:\.(?:[2][1-4]\d|25[1-5]|1\d{2}|[1-9]\d|[0-9])){3}(?::\d{4})?|[a-z\-]+(?:\.[a-z\-]+){2,})$/i;
    const regex = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/i;
    if (control.value && control.value.length > 0) {
      if (!regex.test(control.value)) {
        return { invalidUrl: true };
      }
    }

    return null;
  };
}

export function EmailValidator(): ValidatorFn {
  return (control: AbstractControl) => {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (control.value && control.value.length > 0) {
      if (!emailRegex.test(control.value)) {
        return { invalidEmail: true };
      }
    }

    return null;
  };
}

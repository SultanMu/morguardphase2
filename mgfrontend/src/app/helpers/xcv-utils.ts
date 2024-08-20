import * as jstz from 'jstz';

export class XcvUtils {

    public defineTimezoneName(): string {
        let timeZoneName = '';
        try {
          const tz = jstz.determine();
          timeZoneName = tz.name();
        } catch (e) { }
        return timeZoneName;
      }    

}
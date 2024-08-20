
import config from "../../../config.json";
export class APIEndpoints {
    // public static BASE_API = 'http://10.191.0.11:9900';
    public static BASE_API = config.baseUrl;
    public static CLIENT_API = `${this.BASE_API}/client`;
    public static USERS_API = `${this.BASE_API}/users`;
    public static GPT_API = `${this.BASE_API}/llm`;
    public static RECRUITER_API = `${this.BASE_API}/recruiter`;
    public static API_CLIENT = `${this.BASE_API}/api_client`;

}

export class Constants {
    public static ASC = 'ASC';
    public static DESC = 'DESC';
    public static CANCELED = 'CANCELED';
    public static FREE = 'FREE';
    public static STANDARD = 'STANDARD';
    public static PREMIUM = 'PREMIUM';
    public static GPT_CACHE_LIMIT = 14; //means 15
    public static TOOLTIP_POSITION_TOP = 'top';
    public static TOOLTIP_POSITION_BOTTOM = 'bottom';
    public static TOOLTIP_POSITION_LEFT = 'left';
    public static TOOLTIP_POSITION_RIGHT = 'right';
    public static TOOLTIP_DEFAULT_POSITION = this.TOOLTIP_POSITION_TOP;
    public static STARTING_TOKEN = '3000';
    public static STARTING_TOKEN_STANDARD = '5000'; // arbitrary value
    public static STARTING_TOKEN_PREMIUM = '30000'; // arbitrary value
    public static RECRUITER = 'RECRUITER'; // arbitrary value
    public static CLIENT = 'CLIENT'; // arbitrary value
    public static COMPANY = 'COMPANY';
    public static GENERIC_ERROR_MSG = 'An error occurred';
    public static CREATE = 'CREATE'; // this is used on company dashboard. if create, it means company has 0 recruiter and has to create
    public static DISPLAY = 'DISPLAY'; // this means that company has 1 or more recuiter and ready to display
    public static RECRUITER_COST = 14.99;
    public static CLIENT_COST = 9.99;
    // public static IFRAME_STYLE = 'position:absolute;left:0; top:250px; bottom:0; height:100%; width:700px; padding:20px; z-index: 99';
    public static IFRAME_STYLE = 'position:absolute;left:50; top:450px; bottom:0; height:150%; width:800px; padding:20px; z-index: 99';
    public static HAS_PARENT = 'HAS_PARENT';
    public static YES = 'YES';
    public static NO = 'NO';
    public static SINGLE = 'single';
    public static TRIPPLE = 'single';
    public static DECUPLE = 'decuple';
}

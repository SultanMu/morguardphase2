import { Constants } from "app/helpers/app-settings";

export class UserProfile {
    constructor(
        public id?:string,
        public profile?: string,
        public revisedprofile?: string,
        public skills?:any[],
        public experience?:any[],
        public education?:any[],
        public details?:{},
        public tools?:any[],
    )
    {}
}

export class AppUser {
    constructor(
        public id?:string,
        public email?: string,
        public name?: string,
        public token?: string,
        
    )
    {}
}

export class RecruiterResp {
    constructor(
        public total_recruiters?:number,
        public recruiters_data?: Recruiter[]
    )
    {}
}

export class Recruiter {
    constructor(
        public recruiter_email?:string,
        public first_name?: string,
        public last_name?: string,
        public created?: Date,
        public bill?: any,
        public client_count?: number,
        public date_loggedin?: Date,
        public recruiter_clients?: any[],
        // public recruiter_clients?: RecruiterClient[],
        public date_subscribed?: Date,
        public registered?: boolean
    )
    {}
}

export class RecruiterClient {
    constructor(
        public vanity_name?: string,
        public first_name?: string,
        public last_name?: string,
        public recruiter_email?: string,
        public data_pulled?: Date,
        public date_subscribed?: Date
    )
    {}
}

export class Company {
    constructor(
        public company_name?:string,
        public email?: string,
        public total_recruiters?: any,
        public phone?: any,
        public date_subscribed?: Date
    )
    {}
}

export class Client {
    constructor(
        public unique_id?:string,
        public vanity_name?: string,
        public first_name?: string,
        public last_name?: string,
        public tokens_consumed?: string,
        public tokens_limit?: string,
        public date_subscribed?: Date
    )
    {}
}

export class SubscriptionPlan {
    constructor(
        public active?:boolean,
        public aggregate_usage?:any,
        public amount?:number,
        public amount_decimal?:string,
        public billing_scheme?:string,
        public created?:Date,
        public currency?:string,
        public cust_id?:string,
        public id?:string,
        public interval?:string,
        public interval_count?:number,
        public livemode?:boolean,
        public metadata?:any,
        public nickname?:any,
        public object?:string,
        public product?:string,
        public status?:string,
        public sub_id?:string,
        public tiers_mode?:any,
        public transform_usage?:any,
        public trial_period_days?:any,
        public usage_type?:string,
        public plan_type?:string,
        public planType?:string
    )
    {}
}

export class SubscriptionDetails {
    constructor(
    public active?:boolean,
    public aggregate_usage?:any,
    public amount?:number,
    public amount_decimal?:string,
    public billing_scheme?:string,
    public created?:Date,
    public currency?:string,
    public cust_id?:string,
    public ends_at?:Date,
    public id?:string,
    public interval?:string,
    public interval_count?:number,
    public livemode?:boolean,
    public metadata?:any,
    public nickname?:any,
    public object?:string,
    public payment_type?:number,
    public product?:string,
    public started_at?:Date,
    public status?:string,
    public sub_id?:string,
    public tiers_mode?:any,
    public transform_usage?:any,
    public trial_period_days?:any,
    public usage_type?:string,
    public exception?:string
    )
    {}
}

export class PaymentHistory {
    constructor(
        public p_date_created?:any[],
        public p_payment_type?:any[],
        public p_valid_till?:any[]    
    )
{}
}

export class ProfileContact {
    constructor(
        public email?:any[],
        public phone?:any[],
        public facebook?:any,
        public twitter?:any
    )
    {}
}

export class ProfileDate {
    constructor(
        public day?:any,
        public month?:any,
        public year?:any
    )
    {}
}

export class ProfileSocials {
    constructor(
        public facebook?:any,
        public twitter?:any
    )
    {}
}

export class ProfileProject {
    constructor(
        public description?:string,
        public ends_at?: ProfileDate,
        public ends_date?:Date,
        public starts_at?: ProfileDate,
        public starts_date?:Date,
        public title?:string,
        public url?:string,
        public editMode?:boolean,
        public proId?:any,
    )
    {}
}

export class ProfileEducation {
    constructor(
        public activities_and_societies?:string,
        public degree_name?:string,
        public description?:string,
        public ends_at?:ProfileDate,
        public ends_date?:Date,
        public field_of_study?:string,
        public grade?:string,
        public school?:string,
        public school_linkedin_profile_url?:string,
        public starts_at?:ProfileDate,
        public starts_date?:Date,
        public editMode?:boolean,
        public eduId?:any
    )
    {}
}

export class ProfileExperience {
    constructor(
        public company?:string,
        public company_linkedin_profile_url?:string,
        public description?:string,
        public ends_at?:ProfileDate,
        public ends_date?:Date,
        public location?:string,
        public starts_at?:ProfileDate,
        public starts_date?:Date,
        public title?:string,
        public expId?:any,
        public editMode?:boolean,
        public experienceGPTCache?: ProfileExperienceGPT
    )
    {}
}

export class ProfileExperienceGPT {
    constructor(
        public expDataCurrentArray: Array<any> = [],
        public expDataUndoArray: Array<any> = [],
        public expDataRedoArray: Array<any> = [],
        public expUndoLimit: number = Constants.GPT_CACHE_LIMIT,
        public expShowUndo?:boolean,
        public expShowRedo?:boolean,
    )
    {}
}

export class Profile {
    constructor(
        public hasChanged?:boolean,

        public about?:string,
        public aboutOrig?:string,
        public aboutChanged?:boolean,
        public aboutDataCurrentArray: Array<any> = [],
        public aboutDataUndoArray: Array<any> = [],
        public aboutDataRedoArray: Array<any> = [],
        public aboutUndoLimit: number = Constants.GPT_CACHE_LIMIT,
        public aboutShowUndo?:boolean,
        public aboutShowRedo?:boolean,
      
        public client?:number,

        public contact?: ProfileContact,
        public contactOrig?: ProfileContact,
        public contactChanged?:boolean,
        public contactPhoneChanged?:boolean,
        public contactTwitterChanged?:boolean,

        public country?:string,
        public countryOrig?:string,
        public countryChanged?:boolean,

        public education?:any[], //streamline this later
        public educationOrig?:any[], //streamline this later
        public educationChanged?:boolean,

        public experience?:ProfileExperience[], //streamline this later
        public experienceOrig?:ProfileExperience[], //streamline this later
        public experienceChanged?:boolean,

        public projectChanged?:boolean,

        public first_name?:string,
        public first_nameOrig?:string,
        public first_nameChanged?:boolean,

        public github?:string,

        public languages?:any[], //streamline this later
        public languagesOrig?:any[], //streamline this later
        public languagesChanged?:boolean,

        public languagesDisplay?: string,

        public last_name?:string,
        public last_nameOrig?:string,
        public last_nameChanged?:boolean,

        public full_name?:string,

        public lcoation?:string,
        public lcoationOrig?:string,
        public locationChanged?:boolean,

        public resume?:number,
        public resume_id?:number,
        public section_id?:number,

        public skills?:any[], //streamline this later
        public skillsOrig?:any[], //streamline this later
        public skillsChanged?:boolean,

        public skillsDisplay?: string,

        public title?:string,
        public titleOrig?:string,
        public titleChanged?:boolean,

        public vanity_name?:string,
        public myAtt?:string,

        public certifications?:any[], //streamline this later
        public certificationsOrig?:any[], //streamline this later
        public certificationsChanged?:boolean,
        public certificationsVisible?:boolean,

        public accomplishments?:ProfileAccomplishments, //streamline this later
        public accompishmentsChanged?:boolean,
        public visibilityChanged?:boolean,

        // public publications?:any[], //streamline this later
        // public publicationsOrig?:any[], //streamline this later
        // public publicationsChanged?:boolean,


        public socials?:ProfileSocials,

        public visibility?:ProfileVisibility,
        
        public jd?: any
    )

    {}
}


export class ProfileVisibility {
    constructor(
        public courses?:boolean,
        public projects?:boolean,
        public publications?:boolean,
        public experience?:boolean,
        public skills?:boolean,
        public languages?:boolean,
        public education?:boolean,
        public certifications?:boolean,
        public email?:boolean,
        public linkedin?:boolean,
        public twitter?:boolean,
        public contactno?:boolean
    )
    {}
}

export class ProfileAccomplishments {
    constructor(
        public courses?:ProfileCourse[],
        public coursesChanged?:boolean,
        public coursesVisible?:boolean,
        public publications?: ProfilePublication[],
        public publicationsChanged?:boolean,
        public publicationsVisible?:boolean,
        public projects?: ProfileProject[],
        public projectsChanged?:boolean,
        public projectsVisible?:boolean,
        public honorsVisible?:boolean,
        public test_scores?:any[]
    )
    {}
}

export class ProfileCourse {
    constructor(
        public name?:string,
        public number?:string,
        public editMode?:boolean,
        public couId?:any,
    )
    {}
}

export class ProfilePublication {
    constructor(
        public description?:string,
        public name?:string,
        public published_on?: ProfileDate,
        public published_on_date?: Date,
        public publisher?:string,
        public url?:string,
        public editMode?:boolean,
        public pubId?:any,
    )
    {}
}


export class CompanyProfile {
    constructor(
        public total_recruiters?:string,
        public recruiters_data?:CompanyProfileRecruiterData[],
    )
    {}
}

export class CompanyProfileRecruiterData {
    constructor(
        public recruiter_email?:string,
        public first_name?:string,
        public last_name?:string,
        public date_subscribed?:Date,
        public recruiter_clients?:CompanyProfileRecruiterClient[]
    )
    {}
}

export class CompanyProfileRecruiterClient {
    constructor(
        public first_name?:string,
        public last_name?:string,
        public vanity_name?:string,
        public data_pulled?:Date
    )
    {}
}

export class subcriptionType {
    constructor(
        public payment?:boolean,
        public type?:any
        ){}
}



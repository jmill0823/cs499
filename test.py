from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_response(input_text, max_tokens=2048):
    # Encode the input text and convert to tensors
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate output from the model
    output = model.generate(input_ids, max_new_tokens=max_tokens)

    # Decode and print the output text
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded_output

# Example usage
input_text = """
﻿<!DOCTYPE html>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Re: Call 8/14</title>
<link rel="important stylesheet" href="">
<style>div.headerdisplayname {font-weight:bold;}
</style></head>
<body>
<table border=0 cellspacing=0 cellpadding=0 width="100%" class="moz-header-part1 moz-main-header"><tr><td><b>Subject: </b>Re: Call 8/14</td></tr><tr><td><b>From: </b>&quot;Weinstein, Jessica E.&quot; &lt;Jessica.Weinstein@UKY.EDU&gt;</td></tr><tr><td><b>Date: </b>8/15/21, 8:05 AM</td></tr></table><table border=0 cellspacing=0 cellpadding=0 width="100%" class="moz-header-part2 moz-main-header"><tr><td><b>To: </b>OPHTHOCALL-L@LSV.UKY.EDU</td></tr><tr><td><div class="headerdisplayname" style="display:inline;">Reply-to: </div> Ophthalmology Call Email List <OPHTHOCALL-L@LSV.UKY.EDU></td></tr></table><br>
<html><head>
<meta http-equiv="Content-Type" content="text/html; "></head>
<body>
<div>
<div>
<div dir="ltr" style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);">
That’s the plan, just not emergently</div>
</div>
<div id="ms-outlook-mobile-signature">
<div><br>
</div>
Get <a href="https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2Fo0ukef&amp;data=04%7C01%7Cdaniel.b.moore%40UKY.EDU%7Cfff809719a7349363ea708d95fe4fa23%7C2b30530b69b64457b818481cb53d42ae%7C0%7C0%7C637646259329751445%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&amp;sdata=pc4kEZfe%2BfTlcTcGmSCFfeKYQqJw42%2F2BTNG85yS3Yo%3D&amp;reserved=0" originalsrc="https://aka.ms/o0ukef" shash="MotNblOCUG7R4jqY3ViOMkPiu9v3SjCBWM99nWUn5m0fpSraNLX/+jD8Apm8SCaEcszzAc0kAwIa5GRs2wv+6uqsK6tw6WraFW3piKj+WLx70UkjJ6hvV7XRF7MM9Vtlh9LC6EKI8UyUUNAnbWsQVR5apqhbBkv8HtmeKidUC9s=" originalsrc="https://aka.ms/o0ukef" shash="EUyc3mVtC0ulCxHoC8mlmXgJ2BOXu6XMYtMlL6yAHR0wq5rMK+zzaxvsuWfvqWozdM7x27QC+K5O0iZsBbQOCCnHeugJw6PtsjP0GthNyP+WPESFh5hV5wXdFGv+jx8tfyC3Rxt/FfSErVAwWp+KPJhfJzz9wQBcT4dqNvU+NIk=">
Outlook for iOS</a></div>
</div>
<hr style="display:inline-block;width:98%" tabindex="-1">
<div id="divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" style="font-size:11pt" color="#000000"><b>From:</b> Ophthalmology Call Email List &lt;OPHTHOCALL-L@LSV.UKY.EDU&gt; on behalf of Pearson, Andrew &lt;apear1@UKY.EDU&gt;<br>
<b>Sent:</b> Sunday, August 15, 2021 7:31:46 AM<br>
<b>To:</b> OPHTHOCALL-L@LSV.UKY.EDU &lt;OPHTHOCALL-L@LSV.UKY.EDU&gt;<br>
<b>Subject:</b> Re: Call 8/14</font>
<div>&nbsp;</div>
</div>
<div dir="auto">Just curious - why not do vtx on Doe?<br>
<br>
<div dir="ltr">Andrew Pearson, MD
<div>Professor and Chairman<br>
<div>University of Kentucky</div>
<div>Dept of Ophthalmology and Visual Science</div>
<div>859-323-5868 (o)</div>
<div>859-227-4653 (c)</div>
<div>Sent from my iPhone</div>
</div>
</div>
<div dir="ltr"><br>
<blockquote type="cite">On Aug 15, 2021, at 7:15 AM, Weinstein, Jessica E. &lt;Jessica.Weinstein@uky.edu&gt; wrote:<br>
<br>
</blockquote>
</div>
<blockquote type="cite">
<div dir="ltr">﻿
<div>
<div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)">For Jane Doe&nbsp;</div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)"><br>
</div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)">1)can they attempt challenge with Voriconazole to see if it would also prolong QTC? Any other non triazoles?</div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)"><span style="font-size:inherit"><br>
</span></div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)"><span style="font-size:inherit">2) Patient likely needs rehab program - social work consult, unclear if she’s taking her methadone…</span></div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)"><span style="font-size:inherit"><br>
</span></div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)">3) please advise needs anti fungal ampho or she may lose her eye. We discussed weekly dosing for tx vs prep for OR débridement…. Especially if we don’t get anti fungal on board, this
 is even more important.&nbsp;</div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)"><br>
</div>
<div dir="ltr" style="color:rgb(0,0,0); background-color:rgb(255,255,255)">Thanks</div>
</div>
<div id="x_ms-outlook-mobile-signature">
<div><br>
</div>
Get <a href="https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2Fo0ukef&amp;data=04%7C01%7Cdaniel.b.moore%40UKY.EDU%7Cfff809719a7349363ea708d95fe4fa23%7C2b30530b69b64457b818481cb53d42ae%7C0%7C0%7C637646259329751445%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&amp;sdata=pc4kEZfe%2BfTlcTcGmSCFfeKYQqJw42%2F2BTNG85yS3Yo%3D&amp;reserved=0" originalsrc="https://aka.ms/o0ukef" shash="MotNblOCUG7R4jqY3ViOMkPiu9v3SjCBWM99nWUn5m0fpSraNLX/+jD8Apm8SCaEcszzAc0kAwIa5GRs2wv+6uqsK6tw6WraFW3piKj+WLx70UkjJ6hvV7XRF7MM9Vtlh9LC6EKI8UyUUNAnbWsQVR5apqhbBkv8HtmeKidUC9s=" originalsrc="https://aka.ms/o0ukef" shash="clMLEVMduC1+X0ZXnBD26EjGsXT0lQm6T7VsagjCqQE85c0oudvF8ZVto2g0/kN57szNFzoc5QQMwBUM9HcFTBMGz2+bkW1+Px7zjF0baM8pfied0TMsf63F+02ixymY8AR9Co4oGwysgn7iJ2VP4338a/+NtrAnvH/BaGUa93A=" originalsrc="https://aka.ms/o0ukef" shash="NkVQS+aYfPiFkWSanNaf/DdVdihj4jM/HU2ra5uLuOSUCp/ywWjmAIZZ7h1Mes2asTGP4jjih/kmK9ryyjJcV0TMuJ8uN4+yvow31X9j+0pI6dkYaXo2ib3Tx1ImFh1LKo+LCKZu/jDzOIXmX2F/6jDIfsmaPIJ9OpzU3UT59I0=">
Outlook for iOS</a></div>
</div>
<hr tabindex="-1" style="display:inline-block; width:98%">
<div id="x_divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" color="#000000" style="font-size:11pt"><b>From:</b> Ophthalmology Call Email List &lt;OPHTHOCALL-L@LSV.UKY.EDU&gt; on behalf of Blosser, Peter E. &lt;Peter.Blosser@UKY.EDU&gt;<br>
<b>Sent:</b> Sunday, August 15, 2021 7:00:03 AM<br>
<b>To:</b> OPHTHOCALL-L@LSV.UKY.EDU &lt;OPHTHOCALL-L@LSV.UKY.EDU&gt;<br>
<b>Subject:</b> Call 8/14</font>
<div>&nbsp;</div>
</div>
<div dir="ltr">
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<span style="font-size:12pt"><b></b><b><b>***Cyclogyl still not available</b>​</b>​***</span></div>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<span style="font-size:12pt"><b></b></span></div>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<span style="font-size:12pt"><b><br>
</b></span></div>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<span style="font-size:12pt"><b>UK</b></span> </div>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<div style="font-size:12pt"><span style="font-size:12pt; font-family:Calibri,Helvetica,sans-serif;">Liam Nelson 456789012 03/04/1996</span></div>
<div style="font-size:12pt"><span lang="EN"></span>
<p style="margin-top: 0px; margin-bottom: 0px;margin-top:0px; margin-bottom:0px; margin-top:0px; margin-bottom:0px; margin-top:0px; margin-bottom:0px">
<font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">39 yo female with PMH anxiety/depression
 who presents as a transfer from Pikeville due to concern for possible retinal detachment in her right eye. On 8/13 she and her ex-husband began arguing, and he slapped her multiple times in the face along with slamming her head against the wall. He also grabbed
 her face and she felt like his fingernail scratched her right eye. She was in significant pain from her right eye so presented to ED in Pikeville. She was evaluated there by the optometrist on call who debrided her corneal abrasion and was concerned for inferior
 RD so referred her to UK for surgical evaluation. Reporting blurry vision in right eye, still having significant pain in the eye. No problems with her left eye.
</span><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;"><b>Exam:&nbsp;</b></span></font></font></font><font size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">VA: sc OD 20/300 ph 20/80 OS 20/60 ph 20/20.
 IOP, EOM wnl. Mild constriction of superior field OD on CVF. Pupils notable for anisocoria OD 8 to 6 in dark, OS 6 to 4 in dark but no APD (was dilated earlier in the day by optometry so suspect anisocoria related to residual effects). SLE OD mild UL/LL ecchymosis/edema;
 small SCH at 9:00; 7x8.5mm central corneal abrasion&nbsp;</span><span style="font-size:11pt"><span style="background-color: rgb(255, 255, 255); display: inline !important; font-family: Calibri, Helvetica, sans-serif; font-size: 12pt;">(involves almost entire cornea)</span></span><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">
 with smaller &lt;1x1mm abrasion peripherally at 2:00 ; 2+ corneal edema with descemet's folds; trace AC cell; otherwise wnl and Schaffer's negative . SLE OS: wnl DFE OD: notable for retinal commotio at 9 o'clock in periphery; possible horseshoe tear at 4 o'clock
 vs vortex vein with pigmentation in mid-periphery; no SRF; no additional holes/tears on scleral depression 360 DFE OS: wnl.
</span></font><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">B-scan</span><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;"><b>
</b></span><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">shows suspicious hyperechoic area inferiorly concerning for retinal tear</span><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;"><b>;
</b></span><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">no SRF and retina flat/attached.
</span></font></font></font><b><font face="Segoe UI" size="3"><font face="Segoe UI" size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">A/P:
</span></font></font></b><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">Possible retinal
 tear right eye - Staffed and examined with Dr. Weldy. Difficult exam due to corneal abrasion so unable to perform laser retinopexy. Follow-up early next week for possible laser retinopexy. RD precautions reviewed</span></font></font></font><font size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">
</span></font><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><font color="#222222" face="Segoe UI" size="3"><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">and patient advised
 to call or return to ED if symptoms worsen</span></font></font></font><font size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">. Corneal Abrasion right eye.
</span><font size="3"><span style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">Traumatic iritis right eye - erythromycin ung qid, atropine bid.
</span></font><b><font face="Segoe UI" size="3"><font face="Segoe UI" size="3"><span lang="EN" style="font-size: 12pt; font-family: Calibri, Helvetica, sans-serif;">Please schedule with Jody Brown in Pikeville on Monday 8/16 . If unable to schedule appointment
 Monday or Tuesday, schedule with UK retina on Tuesday 8/17 (patient with no ride on Monday). (606)123-4567</span></font></font></b></font></p>
</div>
<div><br>
</div>
<div><font color="#000000" face="Calibri">Ethan King &nbsp;543210987 &nbsp;06/23/1971</font></div>
<div><font color="#000000" face="Calibri">9 year old female&nbsp;with PMH migraines who presents to the ED for evaluation of blurry vision after being hit in the left eye with a football that her brother threw on Thursday 8/12. She says that initially the eye was
 red and swollen but that has significantly improved. Her vision has remained blurry, especially in her temporal field with her left eye which is why she was brought to the ED. No vision changes or trouble with her right eye. &nbsp; VA: sc OD 20/20 OS 20/25 ph NI
 &nbsp;IOP, EOM, CVF, Pupils WNL. &nbsp;SLE OD wnl. SLE OS: no periorbital edema or erythema, no staining or evidence of corneal abrasion, AC quiet DFE OD: CDR 0.1; good foveal reflex; wnl &nbsp;DFE OS: CDR 0.1; good foveal reflex; no hemorrhages or areas of commotio; wnl.
 &nbsp;A/P: Blunt force injury to left eye, astigmatism: &nbsp;VA mildly reduced in left eye following injury, suspect transient decrease 2/2 to injury that will likely resolve vs refractive error. Dilated exam wnl OU with no apparent sequelae of trauma. Mother is concerned
 about her ability to see at school without glasses, requests appt early next week.
<strong>Please schedule with pediatrics early next week for repeat DFE and Mrx (school starts Wednesday 8/18) . (289)176-3456 (mother Jane).</strong> &nbsp;
<br>
</font></div>
<div><font color="#000000" face="Calibri"></font><br>
</div>
<div><font color="#000000" face="Calibri">Emma Clark 234567890 05/15/2002</font></div>
<div><font color="#000000" face="Calibri">30 yo F with reported history of recurrent VZV keratitis OD presented to ED due to concern for another VZV flair. ED called requesting assistance with setting up outpatient follow-up, did not ask for patient to be seen.
<span style="display:inline!important; background-color:rgb(255,255,255)">Per ED, patient states that her vision is chronically blurry in the right eye and is no different from baseline.&nbsp;</span>Per ED, VA 20/40 OD, 20/20 OS. IOP 13 OU. ED noted dendritic staining
 on inferior cornea. Briefly visited patient prior to discharge, eye appeared quiet with possible inferior corneal involvement. Patient declined examination. Advised ED to provide erythromycin ung OD qid, Atropine OD bid, and acyclovir 800mg po 5 times daily
 (patient request due to affordability). <b>Please call to schedule follow-up in UCC/general Monday or Tuesday.&nbsp;</b></font><span style="color:rgb(0,0,0); font-family:Calibri"><b>859-328-5769 - will need Spanish interpreter.&nbsp;</b></span></div>
<div><br>
</div>
<div><span style="background-color:rgb(255,255,255)">Noah Johnson 789012345 09/02/1969
<strong>Weinstein</strong></span><br>
</div>
<div><span style="background-color:rgb(255,255,255)"><span style="background-color:rgb(255,255,255)"><span style="background-color:rgb(255,255,255)"><span lang="EN">
<div style="margin-top:0px; margin-bottom:0px">36 yo F with PMH IVDU and Past ocular history of fungal endogenous ophthalmitis of left eye who returns to the ED due to concerns for increased swelling around her left eye with associated pain. She was recently
 discharged after being admitted for treatment of endophthalmitis, s/p vitreous tap and injection of vancomycin, ceftazidime, and voriconazole&nbsp;7/27 and again 8/3; s/p injection of amphotericin B 8/8. Last seen in clinic on 8/11 with Dr. Weinstein, at that time
 exam was stable and plan was for return to clinic in 1 week for possible repeat intravitreal Ampho B. &nbsp;Today she reports continued epigastric/substernal discomfort and weakness, says she feels like something is wrong with her heart. ED reports that her QTC
 is lengthened and are concerned fluconazole may be contributing this. She is currently taking fluconazole 800mg daily, cyclogyl OS tid, and prednisolone OS q2h. Says her pain is improved from what it has been in the past but worse over last day. Denies any
 vision changes. <strong>Exam:</strong>&nbsp;VA: sc OD 20/25 ph 20/20 &nbsp; OS HM 2ft ph NI. &nbsp; IOP, EOM wnl. Pupil OS pharmalogically dilated but no APD by reverse. &nbsp;SLE OD wnl. SLE OS: mild periorbital edema, resolving SCH temporal; inferior fine KP; AC with 1+cell,
 no hypopyon; vitreous with 3-4+ cell and haze, vitreous debris and fungal balls DFE OD: wnl DFE OS: unable to visualize details of nerve or posterior pole due to vitreous haze. B-scan - significant vitreous debris with adhesion to optic nerve; retina appears
 flat and attached.&nbsp;&nbsp;<strong>A/P:</strong> &nbsp;Fungal&nbsp;Endogenous Endophthalmitis&nbsp;of&nbsp;Left eye - Seen with Dr. West and staffed over the phone with Dr. Weldy. Recommended intravitreal amphotericin injection this evening. She declined and stated she would prefer
 to wait due to her other medical issues being evaluated tonight.&nbsp;Discussed antifungal treatment options with ID. Unfortunately there are no other po systemic antifungal options and diflucan contraindicated with prolonged QTC. Recommend admission to medicine
 with ID consult in am to determine systemic antifungal treatment. <b>On call&nbsp;</b><strong>resident to see tomorrow and staff with retina, consider intravitreal ampho B</strong>. Continue pred acetate OS q2h while awake&nbsp;and cyclogyl
<span style="background-color:rgb(255, 255, 255);display:inline !important">OS tid&nbsp;</span>(atropine if not available) .
<span lang="EN">If discharged, keep follow-up as scheduled with Dr. Weinstein on 8/18.</span> 502-642-7146&nbsp;</div>
</span></span></span>
<div><br>
</div>
<div><b>Good Sam</b></div>
<div>Grace Adams &nbsp;567890123 &nbsp;8/10/1984<br>
38 yoM without significant PMH who presents for evaluation of right eye corneal foreign body. Reports that he was grinding metal at work Friday. He thinks he may have had metal on his arms that he wiped into his right eye later when he got home. Was evaluated
 at Ephraim McDowell Saturday with partial removal of foreign body but was told they could not get all of it out. He continued to have eye discomfort so presented to Good Sam for further evaluation. Reporting mild blurry vision when his eye is tearing but otherwise
 no vision changes.&nbsp; &nbsp;<b>Exam:&nbsp;</b>VA: sc OD 20/20 OS 20/20. &nbsp;IOP, EOM, CVF. Pupils round, reactive, no APD; anisocoria OD 4 to 3, OS 6 to 5. &nbsp;SLE OD mild upper lid edema, 1+ conj injection; dark, round corneal FB midperiphery at 1:00 not in visual axis; following
 removal &lt;1x1mm epithelial defect, otherwise wnl . SLE OS: wnl DFE OD: small, round &lt;1DD &nbsp;chorioretinal scar at 7:30 in mid periphery &nbsp;DFE OS: wnl. &nbsp;<b>A/P</b>: Metallic corneal foreign body OD - Removed at slit lamp with 19g needle. Eyelids everted and fornices
 swept, no other foreign bodies seen on exam. Erythromycin ung OD qid; Cyclogyl 1% OD bid for photophobia
<b>Please schedule with general/UCC for follow-up early next week . 606-282-0679&nbsp;</b><br>
</div>
<div><br>
</div>
</span>
<div><b><b>Follow-up</b></b></div>
</div>
<div style="font-size:12pt"><b><span style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont; font-weight:400; display:inline!important; background-color:rgb(255,255,255)">Samuel R.<span style="margin:0px">&nbsp;</span></span><span class="x_markjwhy4der3" style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont; font-weight:400; background-color:rgb(255,255,255)">Wilson</span><span style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont; font-weight:400; display:inline!important; background-color:rgb(255,255,255)"><span style="margin:0px">&nbsp;</span>4/27/1978
    890123456 </span><span style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont; display:inline!important; background-color:rgb(255,255,255)">Katz</span><br>
</b></div>
<div style="font-size:12pt"><span style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont; display:inline!important; background-color:rgb(255,255,255)"><span style="display:inline!important; background-color:rgb(255,255,255)">43 year
 old female, CL wearer, here for follow up of corneal ulcer of the left eye.&nbsp;&nbsp;Seen by&nbsp;</span><span style="margin:0px; background-color:white"><span>by Dr. Katz Thursday, noted to have descemetocele that was repithelialized. Started Amphotericin on 8/12, alternating
 q1h with Natamycin. Also on Vanc/Tobra qid. </span><b>Update:</b>&nbsp;Cultures previously growing mold, speciated to fusarium, otherwise NGTD. Symptomatically stable, does report seeing more colors with left eye today. VA 20/20 OD, HM OS. Right pupil round and
 reactive, unable to visualize left pupil but no APD by reverse. IOP 14|10. SLE: OD wnl; OS stable area of corneal infiltrate with overlying epi defect, breaking up inferiorly; descemetocele appears re-epitheliazed, Seidel negative; AC deep with no hypopyon.
<span style="margin:0px; display:inline!important; background-color:rgb(255,255,255)">
<span style="margin:0px; background-color:white">Discussed</span></span><b><span style="font-weight:400"> seriousness of condition. Patient understands this is a vision threatening condition and needs close follow-up. Discussed high risk of perforation. absolutely
 no eye rubbing, gentle dab, given clear eye shield to be worn at bedtime. Continue present management with fortified Ampho/Natamycin alternating q1h,&nbsp; vanc/tobra qid,&nbsp; PO doxy 100 mg BID, Vit C, and E mycin ung at bedtime.
</span><span>Patient is scheduled for follow-up with Dr. Katz at Baptist on Monday 8/16. (859)423-1234.</span></b></span></span></div>
<div style="font-size:12pt"><b><span style="font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont; font-weight:400"><br>
</span></b></div>
<div style="font-size:12pt"><span><span style="font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont"><span style="margin:0px; background-color:white"><span style="margin:0px">Aaliyah Turner&nbsp;109876543</span></span><br>
<span style="margin:0px; background-color:white"><span>35 y.o. monocular female w/ PMHx of JRA (not currently on immunosuppression) and POHx uveitis 2/2 RA and secondary glaucoma s/p tube shunt about 20 years ago OU, and retinal detachment OS s/p enucleation
 at age of 13, PCIOL OD (and multiple other procedures), who presented to UK ED 8/6 with lens associated&nbsp;pseudomonal keratitis of right eye (poor hygiene). Acanthamoeba PCR and fungal culture NGTD.&nbsp;Has been staffed with Dr. Katz, Dr. Weinstein. Bscan repeated
 8/13 with Dr. Pearson due to complaint of darker vision (still LP),&nbsp;<b style="font-family:Calibri,Arial,Helvetica,sans-serif; background-color:rgb(255,255,255)"><span style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont"><span style="margin:0px; background-color:white"><span style="margin:0px; font-weight:400">l</span><span style="margin:0px; font-weight:400; display:inline!important; background-color:rgb(255,255,255)">ikely
 PVD with traction (stable),&nbsp;</span><span style="margin:0px; font-weight:400">no retinal detachment.
</span></span></span></b>&nbsp;</span><b>Update: </b>Reports that vision was brighter last night, dark again this morning like it was the day before. No increase in pain/discomfort. VA LP OD. IOP 14, unable assess pupil. Anterior segment exam stable with severe
 diffuse conj injection and flat bleb, 8x9mm ring shaped infiltrate with small area of central clearing, epi defect now only 1x3mm area inferonasal, mild thinning 3 to 5 o'clock, Seidel negative, AC deep with no hypopyon.&nbsp;<span><span style="display:inline!important; background-color:rgb(255,255,255)">Discussed
 with primary team who will be working with social work to determine appropriate discharge plan.&nbsp;<b style="font-family:Calibri,Arial,Helvetica,sans-serif; background-color:rgb(255,255,255)"><span style="margin:0px; font-family:Calibri,Arial,Helvetica,sans-serif,serif,EmojiFont"><span style="margin:0px; background-color:white"><span style="margin:0px; font-weight:400">Vision
 change possibly secondary to elevated IOP on presentation in setting of known glaucoma (unclear how long IOP had been elevated).</span></span></span></b>&nbsp;Continue fortified T</span>obra and vigamox q2h while awake, emycin ung qhs, cosopt TID, PO vit C/ doxy/
 cipro. </span><b>Continue to see daily.</b><span>&nbsp;Discharge complicated by homelessness/no transportation.&nbsp;</span></span><br>
</span></span></div>
<div><br>
</div>
<div><font color="#000000" face="Calibri"><strong>Hotline</strong></font></div>
<span><font color="#000000" face="Calibri">Jackson Taylor 01/19/1957 678901234</font></span><br>
</div>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<font color="#000000" face="Calibri">43 yoF seen by Dr. Francoeur on Thursday for left upper eyelid abscess. Calling to ask if she should discontinue warm compresses as area has increased slightly in size and appears to be coming to a head. She denies any worsening
 redness, pain, vision, or fevers/chills. Advised her to continue warm compresses as directed and continue Bactrim/Keflex. Advised her to call if symptoms worsen. She also reports that her son recently tested positive for Covid so she will be getting tested
 on Monday. Advised her to call clinic following test to determine protocol for returning to follow-up appt.
<b>Keep follow-up as scheduled with Dr. Francoeur 8/20.&nbsp;</b></font></div>
<div><br>
</div>
<div><font color="#000000" face="Calibri">Stella Davis 12/14/1997 876543210<strong>
Sanders</strong></font></div>
<div><font color="#000000" face="Calibri">49 yoM with history of advanced OAG OU with severe/permanent visual impairment with intermittent severe visual phenomena in left eye calling due to new visual disturbance in left eye. States that he has been having
 frequent ocular migraines over the past week which is not new for him; however, starting today he noticed new lights in the center of his vision OS. States that there are several lights and they seem to move around and leave a trail of light, reports that
 his vision is a little blurry as the lights are blocking part of his vision. Denies any new floaters, photopsias, or loss of visual field. Per chart review, he has had significant work-up for light phenomenon in past with no specific etiology identified. Suspect
 these new symptoms are related to previously noted visual phenomenon but etiology unclear. Patient has previously scheduled follow-up with Dr. Sanders on Tuesday. Offered to see patient in clinic tonight vs continued monitoring of symptoms. He prefers to observe
 for now. Advised to call again if symptoms worsen. RD precautions reviewed. <strong>
Follow-up as scheduled with Dr. Sanders 8/17. </strong></font></div>
<div><font color="#000000" face="Calibri"><br>
</font></div>
<span>
<div><font color="#000000" face="Calibri"><br>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<br>
</div>
</font></div>
</span>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<span><font color="#000000" face="Calibri">Thanks,</font></span></div>
<div style="color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; font-size:12pt">
<span><font color="#000000" face="Calibri">Peter Blosser</font></span></div>
<br>
<hr>
<p align="center">To unsubscribe from the OPHTHOCALL-L list, click the following link:<br>
<a href="http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1" target="_blank">http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1</a>
</p>
</div>
<br>
<hr>
<p align="center">To unsubscribe from the OPHTHOCALL-L list, click the following link:<br>
<a href="http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1" target="_blank">http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1</a>
</p>
</div>
</blockquote>
<br>
<hr>
<p align="center">To unsubscribe from the OPHTHOCALL-L list, click the following link:<br>
<a href="http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1" target="_blank">http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1</a>
</p>
</div>
</body>
</html>
<br>
<hr>
<p align="center">To unsubscribe from the OPHTHOCALL-L list, click the following link:<br>
<a href="http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1" target="_blank">http://lsv.uky.edu/scripts/wa.exe?SUBED1=OPHTHOCALL-L&amp;A=1</a>
</p>
</body>
</html>
</table></div>

What is the patient's name?
"""
print(generate_response(input_text))

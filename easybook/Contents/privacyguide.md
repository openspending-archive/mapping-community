# How to publish spending data without disclosing personal information

<div class="well">
by OpenSpending team and Ian Makgill, Ticon
</div>

This guide is purposed to help governments to publish spending without compromising personal information. It has been drafted with UK local councils and other public authorities who wish to publish transactional spending in accordance with the UK regulations, but who are concerned if their data include personal information (such as personal names or addresses). While we recognise that governmental accounting systems as well as privacy regulations differs vastly across countries, we think this guide provide key practical advice, which should to some extent be replicable.


## Background

In January 2013 a freelance data specialist from the community used OpenSpending to identify a number of privacy breaches in an individual dataset published by a local council. This was due to inconsistent redaction of sensitive data by the local authority. Whilst the majority of these payments were to organisations (hence probably not highly sensitive), there were also a few unredacted payments to individuals. The person who uploaded the data immediately notified their local council, who in turn referred this to their audit committee. As a precaution the dataset in question, the UK Local Council &pound;500 spending data was taken off the site immediately.

Data privacy should never be a valid justification for shutting off access to public spending information, as there should be simple processes in place to prevent private data from being published. As more spending data becomes public, government agencies will have to implement release procedures, which prevents privacy breaches. For the financial transparency community the data privacy issue represents a challenge, as governments might be tempted to use this as reason for limiting public disclosures.


## So why are we writing this guide?

* because we care about  <a class="c1" href="http://blog.okfn.org/2013/02/22/open-data-my-data/">privacy of individual citizens</a>

* because we care about Open Data, we think it is vital part of making Government transparent and accountable

* because the presence of personal data within transactional spending data has been identified as a barrier for making such data available to the public. (In April 2013 Copenhagen City Council rejected a Freedom of Information request for 1 mi. transactions worth EUR 2.5bn due to the fact that the data contained personal data, which could not be removed without extensive use of personal resources.)


## What are the rules on data privacy and obligations for publishing transactional level spending data?

Incidents of privacy breaches highlights the importance of proper procedures to ensure that data from public sector bodies is properly redacted before being published. The UK government produces a <a class="c1" href= "http://data.gov.uk/blog/local-spending-data-guidance">guideline document for data publishers</a>, which ensures that issues like this are prevented and hence very rare.

The Local Governments Association (UK) has published this <a class="c1" href="http://localnewcontracts.readandcomment.com/appendix-c-inclusions-and-exemptions-for-publishing-data-2/">guide</a>.


## Understanding the problem

In a broad sense, the law is quite simple: you can't publish anything that might identify an individual. Complying with the law is less straightforward. It would be nice if we could just search our output files for for all the occurrences of "Mr.", "Mrs." or "Miss" and redact accordingly, but personal data is often quite difficult to locate and successfully repressing the data requires diligent checking and good organisational practices. 

To complicate matters, many companies and organisations use personal names as their identifiers. Many companies in the Companies House register include &ldquo;Mr.&rdquo; in their name, and there's still more companies with titles that could be confused with personal names.


## Where personal information is usually found in spending data

The primary source of personal data is in the &ldquo;name&rdquo; field from the transaction. Ensuring that this data has been cleansed is likely to ensure that most of your potential breaches have been resolved. However, at times transactions can include privacy sensitive information in the &ldquo;description&rdquo; field of the invoice which could include name, case file or social security number. For this reason all columns in the dataset should be analysed.

Columns to pay special attention to:

<ol>
<li>Name</li>

<li>Address</li>

<li>Narrative / description</li>

<li>Department</li>

<li>Category</li>
</ol>

### Identifying names

There are a number of typical indicators that the payment is made to an individual:

<ol>
<li>Use of "Mr", "Mrs", "Miss" etc at the start of the supplier name</li>

<li>Use of an initial followed by a name e.g. "D. Harrison"</li>

<li>Payment is not associated with an invoice</li>

<li>The payment instruction details specify a refund or specifics such as "Direct Payment"</li>
</ol>

It is possible to use a procedure called 'pattern matching' that can highlight any items in a database that match a certain pattern of characters. Using these routines will make it possible to highlight entries that may include personal name data.

Globally it seems to vary to what extent countries will allow
companies and sole proprietorships to be disclosed to the public.

<h2 class="c3"><a name="h.sxy4odoqd9n2" id="h.sxy4odoqd9n2"></a>How to address
the issue of personal data?

As mentioned before the most important field in spending data is the supplier name, as this will most likely contain the most valuable personal data, but publishers need to be aware of the potential for identities to be triangulated from additional data, such as narratives and transaction descriptions. It is therefore necessary to review all fields in a data set.

<h3>Step 1: Flagging at source</h3>

Evaluating the entries in the supplier name field to assess whether the data includes an individual's name is an inefficient and largely ineffective method for flagging personal data breaches. Instead the most effective method of suppressing publication of this data is to ensure that personal data is flagged as such when payments are made. Every Department in the Council will have a legitimate reason for issuing payments to an individual, so it is advisable to establish an organisation-wide protocol for flagging payments to individuals. Most Councils (UK) have a standard procedure for co-ordinating payments that includes raising a purchase order (PO). Users that generate POs for payments to individuals should simply append a predetermined code to the recipients name, which can then in turn be picked up by the IT department so that the data can be suppressed before publication.

<h3>Step 2: Monitoring the Supplier Database</h3>

The data used in payment reports will originate from the organisation's finance system, which includes a record of suppliers to whom payments are made. To prevent fraud, there is normally a strict procedure for adding suppliers to this database, this procedure should include a requirement that any personal data is flagged for later suppression, effectively creating a second filter to prevent personal data breaches. It is important to note that this procedure should not form the primary prevention mechanism, as the name in the supplier field is often simply not enough to identify whether a payment is for an individual or not, however, this step should be used in order to flag any payments that appear to be to an individual.

<h3>Step 3: Pre publication reviews</h3>

All data that is to be published should go through a two-stage pre-publication review. The first part should include an automated review of the data, where a script is used to select entries that look like they may include personal data.

The scripts should be capable of screening for the following:

<ol class="c6" start="1">
<li>Pre-determined flags that show that a payment is to an individual.</li>

<li>Common pattern matches used in names (e.g. "Miss")</li>

<li>Names of payees that are known to the Council, (e.g. they have been identified as personal payments before)</li>

<li>Any specific funding codes that are likely to indicate that a payment is going to an individual (e.g. Social Care Direct Payments).</li> </ol>

Once data has been selected, it should be reviewed manually to confirm whether the data provides sufficient information to identify an individual. There is no need to manually review data that has already been flagged as an individual by the Department making the payment, or has been previously been identified as an individual through previous work to prevent breaches. Data that has been flagged because it triggered a pattern match or through a funding code should be checked manually.

Once a data line has been identified as a payment to an individual, then the key pieces of text should be stored as a record that allows the Council to suppress that data in the future, (see step 3 above) and for use in the automated flagging procedures for ensuing months.

A further, manual review needs to be undertaken to ensure that personal payments are not missed. Typically payments to individuals will involve small sums (relative to the amount paid to companies) in a small number of transactions. Therefore ordering the data by the lowest value transactions and then looking through the payment lines to try and identify any payments to individuals. Care should be taken to ensure that reviewers are aware of the potential for foreign names to appear in the text and steps should be taken to ensure that a foreign language review is undertaken where necessary. Although this work sounds onerous, in actuality it is a very small task; a regular monthly review should occupy just minutes of staff time, not hours.


<h3>Step 4: Removing data</h3>

You should never delete whole rows of data, instead you should over-write any data that might constitute a data breach. In particular, there should be no reason for removing either date or value fields from a transaction as these cannot be used to identify an individual. Additional data such as department and narrative information should only be overwritten if it contains data that could identify an individual. Councils should also take steps to detail why the data has been censored. For example, it would be suitable to replace a person's name with the following "Redacted to comply with the Data Protection Act". Providing this additional information gives the data user a good understanding of the nature of the underlying data and advises data consumers that the Council is undertaking it's role as a data producer responsibly.



## <a name="h.wi2gl3oiyddl" id="h.wi2gl3oiyddl"></a>What not to do: The use of overly restrictive disclosure procedures

Data privacy issues should never act as justification for avoiding public disclosure. An example of this, might be the suppression of spend data to a Barrister, on the grounds that the data could be used to identify the individual. Whilst it is right to suppress personal data, the Barrister will be the member of a Chamber of Barristers and any transaction could be allocated to the Chambers rather than to the individual Barrister. The same applies to payments to Doctors, payments should be allocated to the Doctor's practice, not to the individual Doctor concerned.

Ticon has noticed a worrying trend of Councils to redact data on the basis that the payment was made to a 'sensitive supplier', or that the transaction was 'commercially sensitive'. The LGA cites the issues of arbitration, commercial confidence and transactions relating to the underwriting of debt as suitable reasons to redact spend information (see below).

<a href="#" name="db587461f48ca9d947b08d54b3901ee8dd196ccf" id=
"db587461f48ca9d947b08d54b3901ee8dd196ccf"></a><a href="#" name="0"></a>

<table border="1" cellpadding="0" cellspacing="0" class="c58">
<tbody>
<tr class="c25">
<td class="c38">
No
</td>

<td class="c29">
Examples of transactions that may be excluded
from publication
</td>

<td class="c17">
Reason
</td>

<td class="c35">
Redacted or Excluded
</td>
</tr>

<tr class="c25">
<td class="c38">
1
</td>

<td class="c29">
Salary payments to staff (including bonuses), except when
published under the senior salary scheme. These will be published
separately
</td>

<td class="c17">
Personal information protected by the Data Protection
Act
</td>

<td class="c35">
Excluded
</td>
</tr>

<tr class="c25">
<td class="c38">
2
</td>

<td class="c29">
Pension contributions (excluding service charge)  and
National Insurance Contributions
</td>

<td class="c17">
Personal information protected by the Data Protection
Act
</td>

<td class="c35">
Excluded
</td>
</tr>

<tr class="c25">
<td class="c38">
3
</td>

<td class="c29">
Severance payments
</td>

<td class="c17">
Personal information protected by the Data Protection
Act
</td>

<td class="c35">
Excluded
</td>
</tr>

<tr class="c25">
<td class="c38">
4
</td>

<td class="c29">
Payments to individuals from legal process -
compensation payments, legal settlements, fraud payments
</td>

<td class="c17">
Personal information protected by the Data Protection
Act
</td>

<td class="c35">
Redacted

(in exceptional cases exclude the data)
</td>
</tr>

<tr class="c25">
<td class="c38">
5
</td>

<td class="c29">
Competition prizes &ndash; where a normal part of
operations
</td>

<td class="c17">
Personal information protected by the Data Protection
Act
</td>

<td class="c35">
Redacted
</td>
</tr>

<tr class="c25">
<td class="c38">
6
</td>

<td class="c29">
Settlements made with companies as an arbitration which is
conditional on confidentiality
</td>

<td class="c17">
Commercial-in-confidence &ndash; exempt under
FOI
</td>

<td class="c35">
Redacted
</td>
</tr>

<tr class="c25">
<td class="c38">
7
</td>

<td class="c29">
Potential betrayal of a commercial confidence, or prejudice
to a legitimate commercial interest
</td>

<td class="c17">
Very rare and will need to be justified
</td>

<td class="c35">
Redacted
</td>
</tr>

<tr class="c25">
<td class="c38">
8
</td>

<td class="c29">
Transactions relating to the financing or underwriting of
debt e.g. purchase of credit default swaps
</td>

<td class="c17">
Outside the definition of expenditure for this
purpose
</td>

<td class="c35">
Excluded
</td>
</tr>

<tr class="c25">
<td class="c38">
9
</td>

<td class="c29">
Provisions or promises to pay not yet realised
</td>

<td class="c17">

</td>

<td class="c35">
Excluded
</td>
</tr>
</tbody>
</table>

If Councils are to be genuinely open about their activities, there should be no suppression of payments to a commercial entity listed in Companies House (or any other Companies register). Individual companies can chose to protect their tender submissions and other commercial data that they send to the Council from release under the Freedom of Information Act, however, there really should be no position where the simple fact of a payment is seen as commercially sensitive. Whilst the suppression of data on payments to companies as part of settlements is a common legal practice, Councils should do their utmost to resist activity which is so protectionist and undemocratic. Perhaps financing payments should be recorded separately, but it is hard to justify their exclusion from open publication.

<h3>Privacy for farmers receiving farm subsidies in EU</h3>

In 2010 the European Court of Justice ruled that mandatory disclosure of names of<a class="c1" href="http://www.ft.com/intl/cms/s/0/16973ef0-ec2d-11df-9e11-00144feab49a.html#axzz2KIkhha4O"> </a> <a class="c1" href="http://www.ft.com/intl/cms/s/0/16973ef0-ec2d-11df-9e11-00144feab49a.html#axzz2KIkhha4O">German recipients from EU farm subsidies</a> amounted to a breach of their privacy. The ECJ decision has not been overturned since and has led to a substantial decrease in access to overall EU spending, due to the large share that the Common Agricultural Programme (CAP) occupy within the total budget. Much like the Barristers, these farms are commercial entities and the farms should be named on each
transaction.

Whilst the need to protect individuals in receipt of non-commercial payments from Government, e.g. Housing Benefit or Pensions payments should be recognised, Open Spending believes that all commercial payments should be published openly. If individuals who receive monies from Government in exchange for services, or as part of a grant for a commercial enterprise need to remain anonymous, they can always choose to reject that payment.

<h3>Summary</h3>

The world is just getting used to the existence of open spending data, but as the data attracts increased usage governments will come under greater pressure to create dependable, consistent and accurate datasets. Now is the time to ensure that your data is correctly presented, free of data that may breach regulations and can be used by organisations like openspending.org.

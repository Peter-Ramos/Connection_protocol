



Education                                                     E.H. Ramos
Internet-Draft                                     University of Piraeus
Intended status: Informational                               19 May 2023
Expires: 20 November 2023


                         Semester project 2023
                      draft-ramos-unipi-project-00

Abstract

   The comunication between client and server for adding, deviding,
   multiplying, subtracting and module of numbers

Status of This Memo

   This Internet-Draft is submitted in full conformance with the
   provisions of BCP 78 and BCP 79.

   Internet-Drafts are working documents of the Internet Engineering
   Task Force (IETF).  Note that other groups may also distribute
   working documents as Internet-Drafts.  The list of current Internet-
   Drafts is at https://datatracker.ietf.org/drafts/current/.

   Internet-Drafts are draft documents valid for a maximum of six months
   and may be updated, replaced, or obsoleted by other documents at any
   time.  It is inappropriate to use Internet-Drafts as reference
   material or to cite them other than as "work in progress."

   This Internet-Draft will expire on 20 November 2023.

Copyright Notice

   Copyright (c) 2023 IETF Trust and the persons identified as the
   document authors.  All rights reserved.

   This document is subject to BCP 78 and the IETF Trust's Legal
   Provisions Relating to IETF Documents (https://trustee.ietf.org/
   license-info) in effect on the date of publication of this document.
   Please review these documents carefully, as they describe your rights
   and restrictions with respect to this document.  Code Components
   extracted from this document must include Revised BSD License text as
   described in Section 4.e of the Trust Legal Provisions and are
   provided without warranty as described in the Revised BSD License.







Ramos                   Expires 20 November 2023                [Page 1]

Internet-Draft            Semester project 2023                 May 2023


Table of Contents

   1.  Introduction  . . . . . . . . . . . . . . . . . . . . . . . .   2
     1.1.  Requirements Language . . . . . . . . . . . . . . . . . .   2
   2.  Terminology . . . . . . . . . . . . . . . . . . . . . . . . .   2
   3.  Protocol Overview . . . . . . . . . . . . . . . . . . . . . .   3
   4.  Protocol Header Format  . . . . . . . . . . . . . . . . . . .   3
     4.1.  First header  . . . . . . . . . . . . . . . . . . . . . .   3
     4.2.  Second header . . . . . . . . . . . . . . . . . . . . . .   4
   5.  Acknowledgements  . . . . . . . . . . . . . . . . . . . . . .   5
   6.  IANA Considerations . . . . . . . . . . . . . . . . . . . . .   5
   7.  Security Considerations . . . . . . . . . . . . . . . . . . .   5
   8.  Informative References  . . . . . . . . . . . . . . . . . . .   5
   Author's Address  . . . . . . . . . . . . . . . . . . . . . . . .   5

1.  Introduction

   The comunication between client and server is using 3 different types
   of protocols.  2 types for the call request, because the amount of
   numbers used in different mathematical operations, and 1 for the
   response

   This document follows the keyword use as specified in RFC2119
   [RFC2119].

   The terminology is:

   a.  symbols

   b.  numbers

   c.  letters

   d.  hanging

1.1.  Requirements Language

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
   document are to be interpreted as described in RFC2119 [RFC2119].

2.  Terminology

   This document uses the following terms:

      Protocol - A pre-approved communication language between two end
      systems.




Ramos                   Expires 20 November 2023                [Page 2]

Internet-Draft            Semester project 2023                 May 2023


      Server - The part of the communication protocol that receives the
      request.  In this project the server is an endpoint for a
      database.

      Client - The part of the communication protocol that starts the
      request.  In this project the client is a student application that
      requests subscription to the student's database.

      byte - An 8-bit octet

3.  Protocol Overview

   Figure 1 provides a detailed high-level overview of the message
   exchange between the server and the client.

                       Server                    Client
                          v                        |
                     Server Socket                 |
                     Create                        v
                          |                   Client socket
                          |                   create
                          |                        |
                          v                        v
                     Read Datagram <-------- Create datagram
                          |                        |
                          v                        |
                    Calculate answer               |
                          |                        |
                          v                        v
                   Create datagram ---------> Read datagram
                   with the answer                 |
                          |                        v
                          |                   wait and close
                                              client socket

                         Figure 1: Message Exchange

4.  Protocol Header Format

   The following headers are required in order to satisfy all the
   requirements

   Each header SHOULD be in a different subsection

4.1.  First header

   This is the first message sent by the Client to initiate the
   communication process...



Ramos                   Expires 20 November 2023                [Page 3]

Internet-Draft            Semester project 2023                 May 2023


   The following figure shows the message format.

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |        Message Type           |            Length             |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |        Message ID             |           Operation           |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                         Figure 2: A Header Format

   *  Message Type - 16 bits unsigned integer: The message type.  For
      this message, the message type MUST be 0.

   *  Length - 16 bits unsigned integer.  The value for this message
      MUST be 12 or 14 or 16, depending on the type of the operation.

   *  Message ID - 16 bits unsigned integer: The ID of the client.

   *  Operation - 16 buts unsigned integer: The value of the message is
      in range [0,4], depending on the type of operation needed

4.2.  Second header

   This is the second header by the Server to complete the communication
   process...

   The following figure shows the message format.

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |        Message Type           |         Response code         |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                           Return ID                           |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                         Figure 3: A Header Format

   *  Message Type - 16 bits unsigned integer: The message type.  For
      this message, the message type MUST be 0.

   *  Response code - 16 bits unsigned integer: The value ranges from 0
      to 2 depending on errors that have occurred

   *  Return ID - 32 bits unsigned integer: The ID of the client.




Ramos                   Expires 20 November 2023                [Page 4]

Internet-Draft            Semester project 2023                 May 2023


5.  Acknowledgements

   The author would like to acknowledge all the Professors who will read
   this Document and thank them for their time and patience.

6.  IANA Considerations

   This memo makes no requests to IANA.

   You could though! ;)

7.  Security Considerations

   The security considerations are specified here:

   Out of bounds numbers - The server does check if every number is in
   the boundaries for each type of operation

   Identification check - The client checks if the id returned from the
   Server is the same id that was sent to the server

   Operation check - Server checks if the number that specifies the
   mathematical operation is in the right boundaries

8.  Informative References

   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119,
              DOI 10.17487/RFC2119, March 1997,
              <https://www.rfc-editor.org/info/rfc2119>.

Author's Address

   Petros Ioannis Ramos
   University of Piraeus
   Department of Digital Systems
   18534 Piraeus
   Greece
   Email: petrosram3@gmail.com












Ramos                   Expires 20 November 2023                [Page 5]

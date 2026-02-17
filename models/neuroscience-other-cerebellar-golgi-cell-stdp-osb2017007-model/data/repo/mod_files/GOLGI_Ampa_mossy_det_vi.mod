TITLE 

COMMENT
ENDCOMMENT

NEURON {
	POINT_PROCESS Golgi_MF_syn
	USEION ca_nmda READ ca_nmdai
	USEION camk2_full READ camk2_fulli VALENCE 1
	NONSPECIFIC_CURRENT i
	RANGE Q10_diff,Q10_channel
	RANGE R, g, ic,yuno
	RANGE Cdur, Erev 
	RANGE r1FIX, r2, r3,r4,r5,gmax,r1,r6,r6FIX,kB
	RANGE tau_1, tau_rec, tau_facil, U	 
	RANGE PRE,T,Tmax, w, lr
		
	RANGE diffuse,Trelease,lamd
	RANGE M,Diff,Rd,O
	
	RANGE tspike
	RANGE nd, syntype, gmax_factor
}

UNITS {
	(nA) = (nanoamp)	
	(mV) = (millivolt)
	(umho) = (micromho)
	(mM) = (milli/liter)
	(pS) = (picosiemens)
	(nS) = (nanosiemens)
	(um) = (micrometer)
	PI	= (pi)		(1)
    }
    
    PARAMETER {
	syntype
	gmax_factor = 1
	Q10_diff	= 1.5
	Q10_channel	= 2.4
	: Parametri Postsinaptici
	gmax		= 2000   (pS)	

	U 			= 0.43 (1) 	< 0, 1 >
	tau_rec 	= 8 (ms) 	< 1e-9, 1e9 > 	 
	tau_facil 	= 5 (ms) 	< 0, 1e9 > 	

	M			= 21.515	: numero di (kilo) molecole in una vescicola		
	Rd			= 1.03 (um)
	Diff		= 0.223 (um2/ms)
		 
	Cdur		= 0.3	(ms)		 
	r1FIX		= 5.4		(/ms/mM) 	 				
	r2			= 0.82	(/ms)			 
	r3			= 0		(/ms)		 
	r4			= 0		(/ms)		 
	r5			= 0.013	(/ms)			 
	r6FIX		= 1.12	(/ms/mM)		 
	Erev		= 0	(mV)
	kB			= 0.44	(mM)

	: Parametri Presinaptici
	tau_1 		= 1 (ms) 	< 1e-9, 1e9 >
	 

	
	u0 			= 0 (1) 	< 0, 1 >	: se u0=0 al primo colpo y=U
	Tmax		= 1  (mM)	
	
	: Diffusion			
	diffuse		= 1
	
	lamd		= 20 (nm)
	nd			= 1
	
	celsius (degC)
	
	alpha1=0.25	:Parameters for the Omega function.
    beta1=80
    alpha2=0.77
    beta2=80
    ca_nmdai			(mM)
	winit= 0.5		(1) :in the code was 1
}


ASSIGNED {
	v		(mV)		: postsynaptic voltage
	i 		(nA)		: current = g*(v - Erev)
	ic 		(nA)		: current = g*(v - Erev)
	g 		(pS)		: conductance
	r1		(/ms)
	r6		(/ms)
	T		(mM)

	Trelease	(mM)
	tspike[100]	(ms)
	x 
	tsyn		(ms)
	PRE[100]
	
	Mres		(mM)	
	numpulses
	tzero
	gbar_Q10 (mho/cm2)
	Q10 (1)
	yuno
	lr
	Area (cm2)
	camk2_fulli (mM)
}

STATE {	
	C
	O
	D
	w (1)
}

INITIAL {
	C=1
	O=0
	D=0
	T=0 (mM)
	yuno = 0
	numpulses=0
	Trelease=0 (mM)
	tspike[0]=1e12	(ms)
	
	Area=0.5
	w=winit
	 
	gbar_Q10 = Q10_diff^((celsius-30)/10)
	Q10 = Q10_channel^((celsius-30)/10)

	: fattore di conversione che comprende molecole -> mM
	: n molecole/(Na*V) -> M/(6.022e23*1dm^3)

	Mres = 1e3 * ( 1e3 * 1e15 / 6.022e23 * M ) : (M) to (mM) so 1e3, 1um^3=1dm^3*1e-15 so 1e15	
	numpulses=0

	FROM i=1 TO 100 { PRE[i-1]=0 tspike[i-1]=0 }  
	tspike[0]=1e12	(ms)
	if(tau_1>=tau_rec){ 
		printf("Warning: tau_1 (%g) should never be higher neither equal to tau_rec (%g)!\n",tau_1,tau_rec)
		tau_rec=tau_1+1e-5
	    } 
	}
		
	FUNCTION imax(a,b) {
	    if (a>b) { imax=a }
	    else { imax=b }
	}
	
FUNCTION diffusione(){	 
	LOCAL DifWave,i,cntc,fi,aaa
	DifWave=0
	cntc=imax(numpulses-100,0)
	FROM i=cntc  TO numpulses{
	    :printf ("%g %g  ",numpulses,fmod(numpulses,10))
	    fi=fmod(i,100)
	    :printf ("%g %g %g __ ",i,numpulses,fi)
	    tzero=tspike[fi]
	    if(t>tzero){
		aaa = (-Rd*Rd/(4*Diff*(t-tzero)))
		if(fabs(aaa)<699){
		    DifWave=DifWave+PRE[fi]*Mres*exp(aaa)/((4*PI*Diff*(1e-3)*lamd)*(t-tzero)) : ^nd nd =1
		}else{
		    if(aaa>0){
			DifWave=DifWave+PRE[fi]*Mres*exp(699)/((4*PI*Diff*(1e-3)*lamd)*(t-tzero)) : ^nd nd =1
		    }else{
			DifWave=DifWave+PRE[fi]*Mres*exp(-699)/((4*PI*Diff*(1e-3)*lamd)*(t-tzero)) : ^nd nd =1
		    }
		}
	    }
	}	
	:printf("\n\n")
	diffusione=DifWave
}

BREAKPOINT {

	if ( diffuse && (t>tspike[0]) ) { Trelease= T + diffusione() } else { Trelease=T }

	SOLVE kstates METHOD sparse
	SOLVE state METHOD cnexp
	g = (gmax + (400 * (2*((w-0)/(1-0))-1))) * gbar_Q10 * O 
	i = (1e-6) *  g * (v - Erev) * gmax_factor
	ic = i
}

DERIVATIVE state {
    lr=eta(ca_nmdai)
    :lr=eta(camk2_fulli)
    :printf("ca_nmdai = %f\n", ca_nmdai)
    w' = lr*(Omega(ca_nmdai)-w)
    :w' = lr*(Omega(camk2_fulli)-w)
	:printf("wp = %f\n", w')
	
    }


KINETIC kstates {
	r1 = r1FIX * Trelease^2 / (Trelease + kB)^2
	r6 = r6FIX * Trelease^2 / (Trelease + kB)^2
	~ C  <-> O	(r1*Q10,r2*Q10)
	:~ O  <-> D	(r3*Q10,r4*Q10)
	~ D  <-> C	(r5*Q10,r6*Q10)
	CONSERVE C+O+D = 1
}

FUNCTION eta(ci (mM)) { : when ci is 0, inv has to be 3 hours.
    LOCAL inv, P1, P2, P3, P4
    P1=100	
    P2=0.002
    P4=1000
    P3=3	: Cube, directly multiplying, see below.
    
    ci=(ci-1e-4)*1e3 	: The function takes uM, and we get mM.
    
    inv=P4 + P1/(P2+(ci*ci*ci*ci))
    eta=1/inv
}	

FUNCTION Omega(ci (mM)) {
    ci=(ci-1e-4)*1e3	: The function takes uM, and we get mM.
    Omega=0.5+1/(1+exp(-(ci-alpha2)*beta2))-0.5/(1+exp(-(ci-alpha1)*beta1))
}


NET_RECEIVE(weight, on, nspike, tzero (ms),y, z, u, tsyn (ms)) {LOCAL fi

: *********** ATTENZIONE! ***********
:
: Qualora si vogliano utilizzare impulsi di glutammato saturanti e'
: necessario che il pulse sia piu' corto dell'intera simulazione
: altrimenti la variabile on non torna al suo valore di default.

INITIAL {
	y = 0
	z = 0
	u = u0
	tsyn = t
	nspike = 1
}
   if (flag == 0) { 
		: Qui faccio rientrare la modulazione presinaptica
		nspike = nspike + 1
		if (!on) {
			tzero = t
			on = 1				
			z = z*exp( - (t - tsyn) / (tau_rec) )	 
			z = z + ( y*(exp(-(t - tsyn)/tau_1) - exp(-(t - tsyn)/(tau_rec)))/((tau_1/(tau_rec))-1) )  
			y = y*exp(-(t - tsyn)/tau_1)			
			x = 1-y-z
			

			if (tau_facil > 0) { 
				u = u*exp(-(t - tsyn)/tau_facil)
				u = u + U * (1+30*u) * (exp(-5*u)- exp(-5))
			} else { u = U }
			
			y = y + x * u
			
			T=Tmax*y
			yuno = y
			fi=fmod(numpulses,100)
			PRE[fi]=y	: PRE[numpulses]=y
			
			:PRE=1	: Istruzione non necessaria ma se ommesso allora le copie dell'oggetto successive alla prima non funzionano!
			:}
			: all'inizio numpulses=0 !			
			
			tspike[fi] = t
			numpulses=numpulses+1
			tsyn = t
			
		}
		net_send(Cdur, nspike)	 
    }
    if (flag == nspike) { 
		tzero = t
		T = 0
		on = 0
    }
}


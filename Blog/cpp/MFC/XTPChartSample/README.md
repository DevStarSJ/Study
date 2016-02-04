stdafx.h에

#include <XTToolkitPro.h> 

추가

(기본적인 h 파일 경로, lib 경로 및 dll 복사 등은 생략)


Resource File (.rc)에서
Dialog Design에 찾아서 아래와 같이 Control을 타이핑

CONTROL         "Chart", IDC_CHARTCONTROL, "XTPChartControl", WS_TABSTOP, 7, 7, 245, 186

Resource.h에 추가

#define IDC_CHARTCONTROL				103

Resource View에서 마우스로 대충 크기 변환
아래와 같은 모양이 됨

IDD_XTPCHARTSAMPLE_DIALOG DIALOGEX 0, 0, 427, 287
STYLE DS_SETFONT | DS_MODALFRAME | DS_FIXEDSYS | WS_POPUP | WS_VISIBLE | WS_CAPTION | WS_SYSMENU
EXSTYLE WS_EX_APPWINDOW
CAPTION "XTPChartSample"
FONT 8, "MS Shell Dlg", 0, 0, 0x1
BEGIN
    DEFPUSHBUTTON   "OK",IDOK,312,266,50,14
    PUSHBUTTON      "Cancel",IDCANCEL,370,266,50,14
    CONTROL         "Chart",IDC_CHARTCONTROL,"XTPChartControl",WS_TABSTOP,7,7,413,255
END

컨트럴에 마우스 우 클릭 Add Variable 누른 뒤 그림대로 추가

이렇게 하면

XTPChartSampleDlg.h 에
public:
	CXTPChartControl m_wndChartControl;

.cpp에

void CXTPChartSampleDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_CHARTCONTROL, m_wndChartControl);
}

가 자동으로 추가

---
void InitChart(); 추가
BOOL CXTPChartSampleDlg::OnInitDialog()에서 InitChart(); 호출

void CXTPChartSampleDlg::InitChart()
{
	// Content를 이용해서 Chart의 Title, Series, Legends등의 설정이 가능
	CXTPChartContent* pContent = m_wndChartControl.GetContent();
	if (!pContent) return;

	// Title 설정
	CXTPChartTitleCollection* pTitles = pContent->GetTitles();
	if (pTitles)
	{
		CXTPChartTitle* pTitle = pTitles->Add(new CXTPChartTitle());
		if (pTitle)
		{
			pTitle->SetText(_T("My Chart"));
		}
	}

	// Series, Series Point 추가
	CXTPChartSeriesCollection* pCollection = pContent->GetSeries();
	if (pCollection)
	{
		CXTPChartSeries* pSeries = pCollection->Add(new CXTPChartSeries());
		if (pSeries)
		{
			pSeries->SetStyle(new CXTPChartLineSeriesStyle());
			CXTPChartSeriesPointCollection* pPoints = pSeries->GetPoints();
			if (pPoints)
			{
				pPoints->Add(new CXTPChartSeriesPoint(0, 3));
				pPoints->Add(new CXTPChartSeriesPoint(1, 1));
				pPoints->Add(new CXTPChartSeriesPoint(2, 2));
				pPoints->Add(new CXTPChartSeriesPoint(3, 0.5));
			}
		}
	}
}
-----
void CXTPChartSampleDlg::InitChart()
{
	// Content를 이용해서 Chart의 Title, Series, Legends등의 설정이 가능
	CXTPChartContent* pContent = m_wndChartControl.GetContent();
	if (!pContent) return;

	// Title 설정
	CXTPChartTitleCollection* pTitles = pContent->GetTitles();
	if (pTitles)
	{
		CXTPChartTitle* pTitle = pTitles->Add(new CXTPChartTitle());
		if (pTitle)
		{
			pTitle->SetText(_T("My Chart"));
		}
	}

	// Series, Series Point 추가
	CXTPChartSeriesCollection* pCollection = pContent->GetSeries();
	if (pCollection)
	{
		CXTPChartSeries* pSeries = pCollection->Add(new CXTPChartSeries());
		if (pSeries)
		{
			pSeries->SetName(_T("Series1"));
			pSeries->SetStyle(new CXTPChartLineSeriesStyle());
			CXTPChartSeriesPointCollection* pPoints = pSeries->GetPoints();
			if (pPoints)
			{
				pPoints->Add(new CXTPChartSeriesPoint(0, 3));
				pPoints->Add(new CXTPChartSeriesPoint(1, 1));
				pPoints->Add(new CXTPChartSeriesPoint(2, 2));
				pPoints->Add(new CXTPChartSeriesPoint(3, 0.5));
			}
		}

		CXTPChartSeries* pS2 = pCollection->Add(new CXTPChartSeries());
		if (pS2)
		{
			pSeries->SetName(_T("Series2"));
			pS2->SetStyle(new CXTPChartLineSeriesStyle());
			CXTPChartSeriesPointCollection* pPoints = pS2->GetPoints();
			if (pPoints)
			{
				pPoints->Add(new CXTPChartSeriesPoint(0, 2));
				pPoints->Add(new CXTPChartSeriesPoint(1, 0.5));
				pPoints->Add(new CXTPChartSeriesPoint(2, 3));
				pPoints->Add(new CXTPChartSeriesPoint(3, 1));
			}
		}

		// SeriesLabel의 설정
		for (int i = 0; i < pCollection->GetCount(); i++)
		{
			CXTPChartSeriesLabel* pLabel = pCollection->GetAt(i)->GetStyle()->GetLabel();
			pLabel->GetFormat()->SetCategory(xtpChartNumber);
			pLabel->GetFormat()->SetDecimalPlaces(1); // 소숫점 표시
			pLabel->SetVisible(FALSE);
		}
	}
}
-----
pContent->GetLegend()->SetVisible(TRUE);
범주 보이게 하기
-----

double dArithmeticMean = pPoints->GetArithmeticMean(0);
double dVariance = pPoints->GetVariance(0);
double dStd = pPoints->GetStandardDeviation(0);

이렇게 각 Point들의 통계값 산출 가능, Min,Max등 여러가지 있음
---
AXIS 설정

		// Axis 설정
		//CXTPChartDiagram2D* pDiagram = DYNAMIC_DOWNCAST(CXTPChartDiagram2D, pCollection->GetAt(0)->GetDiagram());
		CXTPChartDiagram* pDiagram = pCollection->GetAt(0)->GetDiagram();
		CXTPChartDiagram2D* pD2D = DYNAMIC_DOWNCAST(CXTPChartDiagram2D, pDiagram);
		if (pD2D)
		{
			CXTPChartAxis *pAxisX = pD2D->GetAxisX();
			if (pAxisX)
			{
				CXTPChartAxisTitle* pTitle = pAxisX->GetTitle();
				if (pTitle)
				{
					pTitle->SetText(_T("X-Argument"));
					pTitle->SetVisible(TRUE);
				}
			}

			CXTPChartAxis *pAxisY = pD2D->GetAxisY();
			if (pAxisX)
			{
				CXTPChartAxisTitle* pTitle = pAxisY->GetTitle();
				if (pTitle)
				{
					pTitle->SetText(_T("Y-Value"));
					pTitle->SetVisible(TRUE);
				}
			}
		}
-----
		// Marker 안보이게 하기
		for (int i = 0; i < pCollection->GetCount(); i++)
		{
			CXTPChartPointSeriesStyle* pStyle = (CXTPChartPointSeriesStyle*)pCollection->GetAt(i)->GetStyle();
			pStyle->GetMarker()->SetVisible(FALSE);
			//pStyle->GetMarker()->SetSize(20); // Maeker Size 조정
			//pStyle->GetMarker()->SetType(xtpChartMarkerCircle); // enum XTPChartMarkerType 
		}
-----
		pD2D->SetAllowZoom(TRUE);	// 마우스 휠을 이용한 Zoom 허용
		pD2D->SetAllowScroll(TRUE); // Scroll 허용
-----
		m_wndChartControl.SaveAsImage(_T("D:\\A.PNG"),CSize(600,400));





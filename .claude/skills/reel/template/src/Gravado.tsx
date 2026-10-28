/* Reel montado a partir de um vídeo gravado: cortes do vídeo em sequência, headline nos
   primeiros segundos, selo do quadro, legenda em caixa (quando o vídeo não tem), textos
   blocados em momentos marcados, rodapé com identificação e cartão final de CTA. */
import React from 'react';
import { AbsoluteFill, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { CORES_PADRAO, type Cores, type Assinatura } from './tipos';
import { Fontes, pilhaSans, pilhaSerif } from './fontes';
import { CenaVisual } from './cenas';

export type Corte = { inicio: number; fim: number };
export type GravadoProps = {
  cores?: Partial<Cores>;
  fonte?: string;
  fonteItalica?: string;
  /** arquivo em public/ */
  video: string;
  /** trechos do vídeo original, em segundos, na ordem em que entram */
  cortes: Corte[];
  headline?: { texto: string; destaque?: string; duracao?: number; topo?: number; tamanho?: number };
  selo?: string | null;
  /** identificação discreta na base, o vídeo inteiro */
  rodape?: string | null;
  /** legenda em caixa (tempos no vídeo final) */
  legenda?: { inicio: number; fim: number; texto: string }[];
  /** textos blocados em momentos marcados (tempos no vídeo final) */
  textos?: { inicio: number; fim: number; texto: string; topo?: number }[];
  fechamento?: { duracao?: number; chamada?: string; palavra: string; promessa?: string; assinatura?: Assinatura };
  volume?: number;
  /** vídeo gravado espelhado (texto ao contrário): desespelha */
  espelhar?: boolean;
  /** filtro CSS no vídeo, ex.: "brightness(1.15) contrast(1.05)" */
  filtro?: string;
};

export const duracaoGravado = (p: GravadoProps) =>
  p.cortes.reduce((s, c) => s + (c.fim - c.inicio), 0) + (p.fechamento ? p.fechamento.duracao ?? 4.5 : 0);

const useMola = (atraso = 0) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - Math.round(atraso * fps), fps, config: { damping: 16, stiffness: 140, mass: 0.7 } });
};

const Headline: React.FC<{ h: NonNullable<GravadoProps['headline']>; cores: Cores; fonteItalica: string }> = ({ h, cores, fonteItalica }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const e = useMola();
  const dur = h.duracao ?? 2.6;
  const sai = interpolate(frame / fps, [dur - 0.3, dur], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const partes = h.destaque ? h.texto.split(h.destaque) : [h.texto];
  return (
    <div
      style={{
        position: 'absolute', left: 70, right: 70, top: h.topo ?? 190, padding: '34px 44px', borderRadius: 28,
        background: cores.fundo, color: cores.texto, fontFamily: '"Oswald", sans-serif', fontWeight: 700,
        fontSize: h.tamanho ?? 84, lineHeight: 1.05, textTransform: 'uppercase', letterSpacing: '0.005em',
        boxShadow: '0 18px 60px rgba(0,0,0,.35)', opacity: e * sai, transform: `translateY(${(1 - e) * -40}px)`,
      }}
    >
      {partes.map((p, i) => (
        <React.Fragment key={i}>
          {p}
          {i < partes.length - 1 && (
            <span style={{ color: cores.destaque, fontFamily: pilhaSerif(fonteItalica), fontStyle: 'italic', textTransform: 'none', fontSize: (h.tamanho ?? 84) * 1.14 }}>
              {h.destaque}
            </span>
          )}
        </React.Fragment>
      ))}
    </div>
  );
};

const Selo: React.FC<{ texto: string; cores: Cores; fonte: string }> = ({ texto, cores, fonte }) => (
  <div
    style={{
      position: 'absolute', top: 120, left: 0, right: 0, textAlign: 'center', fontFamily: pilhaSans(fonte), fontWeight: 800,
      fontSize: 30, letterSpacing: '0.18em', textTransform: 'uppercase', color: cores.fundo,
      textShadow: '0 2px 14px rgba(0,0,0,.6)',
    }}
  >
    <span style={{ background: cores.destaque, padding: '10px 22px', borderRadius: 999 }}>{texto}</span>
  </div>
);

const Rodape: React.FC<{ texto: string; fonte: string }> = ({ texto, fonte }) => (
  <div
    style={{
      position: 'absolute', bottom: 150, left: 0, right: 0, textAlign: 'center', fontFamily: pilhaSans(fonte),
      fontWeight: 600, fontSize: 24, letterSpacing: '0.02em', color: 'rgba(255,255,255,.92)',
    }}
  >
    <span style={{ background: 'rgba(0,0,0,.45)', padding: '10px 20px', borderRadius: 999 }}>{texto}</span>
  </div>
);

const LegendaCaixa: React.FC<{ itens: NonNullable<GravadoProps['legenda']>; cores: Cores; fonte: string }> = ({ itens, cores, fonte }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const l = itens.find((x) => t >= x.inicio && t < x.fim);
  if (!l) return null;
  const e = interpolate(t - l.inicio, [0, 0.12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ top: 1230, height: 300, justifyContent: 'center', alignItems: 'center', padding: '0 80px' }}>
      <div
        style={{
          background: 'rgba(255,255,255,.96)', color: cores.texto, borderRadius: 26, padding: '22px 36px',
          fontFamily: pilhaSans(fonte), fontWeight: 800, fontSize: 54, lineHeight: 1.18, textAlign: 'center',
          borderLeft: `14px solid ${cores.destaque}`, boxShadow: '0 12px 40px rgba(0,0,0,.35)',
          opacity: e, transform: `translateY(${(1 - e) * 14}px)`, textWrap: 'balance',
        }}
      >
        {l.texto}
      </div>
    </AbsoluteFill>
  );
};

const Textos: React.FC<{ itens: NonNullable<GravadoProps['textos']>; cores: Cores; fonte: string }> = ({ itens, cores, fonte }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const x = itens.find((i) => t >= i.inicio && t < i.fim);
  if (!x) return null;
  const e = interpolate(t - x.inicio, [0, 0.25], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <div
      style={{
        position: 'absolute', left: 70, right: 70, top: x.topo ?? 220, padding: '26px 36px', borderRadius: 24,
        background: cores.destaque, color: cores.sobreDestaque, fontFamily: pilhaSans(fonte), fontWeight: 800,
        fontSize: 46, lineHeight: 1.2, opacity: e, transform: `translateX(${(1 - e) * -30}px)`,
        boxShadow: '0 14px 50px rgba(0,0,0,.35)',
      }}
    >
      {x.texto}
    </div>
  );
};

export const Gravado: React.FC<GravadoProps> = (p) => {
  const { fps } = useVideoConfig();
  const cores: Cores = { ...CORES_PADRAO, ...(p.cores ?? {}) };
  const fonte = p.fonte ?? 'Montserrat';
  const fonteItalica = p.fonteItalica ?? 'Caveat';
  let cursor = 0;
  const blocos = p.cortes.map((c) => {
    const from = Math.round(cursor * fps);
    const dur = Math.max(1, Math.round((c.fim - c.inicio) * fps));
    cursor += c.fim - c.inicio;
    return { from, dur, c };
  });
  const fimVideo = Math.round(cursor * fps);
  const fech = p.fechamento;
  const durFech = Math.round((fech?.duracao ?? 4.5) * fps);
  return (
    <AbsoluteFill style={{ backgroundColor: '#000' }}>
      <Fontes fonte={fonte} fonteItalica={fonteItalica}>
        {blocos.map((b, i) => (
          <Sequence key={i} from={b.from} durationInFrames={b.dur} name={`corte ${i + 1}`}>
            <OffthreadVideo
              src={staticFile(p.video)}
              trimBefore={Math.round(b.c.inicio * fps)}
              trimAfter={Math.round(b.c.fim * fps)}
              volume={p.volume ?? 1}
              style={{ width: '100%', height: '100%', objectFit: 'cover', transform: p.espelhar ? 'scaleX(-1)' : undefined, filter: p.filtro }}
            />
          </Sequence>
        ))}
        <Sequence from={0} durationInFrames={fimVideo} name="sobreposições">
          {p.headline && <Headline h={p.headline} cores={cores} fonteItalica={fonteItalica} />}
          {p.selo && <Selo texto={p.selo} cores={cores} fonte={fonte} />}
          {p.legenda && <LegendaCaixa itens={p.legenda} cores={cores} fonte={fonte} />}
          {p.textos && <Textos itens={p.textos} cores={cores} fonte={fonte} />}
          {p.rodape && <Rodape texto={p.rodape} fonte={fonte} />}
        </Sequence>
        {fech && (
          <Sequence from={fimVideo} durationInFrames={durFech} name="fechamento">
            <AbsoluteFill style={{ backgroundColor: cores.fundo }} />
            <CenaVisual
              cena={{ tipo: 'cta', chamada: fech.chamada, palavra: fech.palavra, promessa: fech.promessa, assinatura: fech.assinatura, fala: '' }}
              cores={cores}
              fonte={fonte}
              fonteItalica={fonteItalica}
              duracao={durFech / fps}
            />
          </Sequence>
        )}
      </Fontes>
    </AbsoluteFill>
  );
};

import AVFoundation
import AppKit
// uso: probe <saida> <video...>  → imprime duração/dimensões, exporta áudio .m4a e 3 quadros .jpg por vídeo
let args = CommandLine.arguments
let out = args[1]
let sema = DispatchSemaphore(value: 0)
for path in args.dropFirst(2) {
  let url = URL(fileURLWithPath: path)
  let asset = AVURLAsset(url: url)
  let dur = CMTimeGetSeconds(asset.duration)
  var dims = "?"
  var fps = 0.0
  if let t = asset.tracks(withMediaType: .video).first {
    let s = t.naturalSize.applying(t.preferredTransform)
    dims = "\(Int(abs(s.width)))x\(Int(abs(s.height)))"; fps = Double(t.nominalFrameRate)
  }
  let base = url.deletingPathExtension().lastPathComponent
  print("\(base) | \(Int(dur)) s | \(dims) | \(Int(fps)) fps | audio: \(asset.tracks(withMediaType: .audio).count)")
  // quadros
  let gen = AVAssetImageGenerator(asset: asset); gen.appliesPreferredTrackTransform = true; gen.maximumSize = CGSize(width: 540, height: 960)
  for (i, frac) in [0.1, 0.5, 0.9].enumerated() {
    let t = CMTime(seconds: dur * frac, preferredTimescale: 600)
    if let cg = try? gen.copyCGImage(at: t, actualTime: nil) {
      let rep = NSBitmapImageRep(cgImage: cg)
      if let d = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.8]) {
        try? d.write(to: URL(fileURLWithPath: "\(out)/\(base)-q\(i).jpg"))
      }
    }
  }
  // áudio
  if let ex = AVAssetExportSession(asset: asset, presetName: AVAssetExportPresetAppleM4A) {
    let a = URL(fileURLWithPath: "\(out)/\(base).m4a"); try? FileManager.default.removeItem(at: a)
    ex.outputURL = a; ex.outputFileType = .m4a
    ex.exportAsynchronously { sema.signal() }; sema.wait()
    if ex.status != .completed { print("  ! áudio falhou: \(ex.error?.localizedDescription ?? "?")") }
  }
}

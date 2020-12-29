D = 'C:\Users\tua_f\Desktop\New folder\Images\crab';
S = dir(fullfile(D,'*'));
%fprintf('S=')
%disp(S)
N = setdiff({S([S.isdir]).name},{'.','..'}); % list of subfolders of D.
for ii = 1:numel(N)
    T = dir(fullfile(D,N{ii},'*')); % improve by specifying the file extension.
    C = {T(~[T.isdir]).name}; % files in subfolder.
    fprintf('C=')
    disp(C)
    for jj = 1:numel(C)
        F = fullfile(D,N{ii},C{jj})
        % do whatever with file F.
    end
end




